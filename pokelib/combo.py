from dataclasses import dataclass
from typing import Iterable
from functools import singledispatch
import time

from .input import GamepadInput
from . import settings

@dataclass
class Hold:
    target: GamepadInput

@dataclass
class Until:
    target: GamepadInput | None = None

class Combo:
    def __init__(self, minimum_interval: float = -1.0) -> None:
        self.pool: list[GamepadInput] = []
        self.minimum_interval = minimum_interval if minimum_interval >= 0.0 else settings.minimum_interval

    def parse(self, iter: Iterable[GamepadInput | int | float]):
        # fasly values: 0, 0.0, [], None, etc.
        li = []
        hold = GamepadInput(0.0)
        interval = 0.0
        for x in iter:
            if isinstance(x, (int, float)):
                interval += x
            elif isinstance(x, GamepadInput):
                if li and interval < self.minimum_interval:
                    interval = self.minimum_interval
                if interval:
                    li.append(GamepadInput(interval) + hold)
                    interval = 0.0
                li.append(x + hold)
            elif isinstance(x, Hold):
                hold = hold + x.target
            elif isinstance(x, Until):
                if x.target:
                    hold = hold - x.target
                else:
                    hold = GamepadInput(0.0)
            else:
                raise ValueError(f"Unsupported type: {type(x)}")
        li.append(GamepadInput(interval))
        self.pool = li
    
    def send(self):
        prev = GamepadInput(0.0)
        for i in self.pool:
            ls = prev.leftstick != i.leftstick
            rs = prev.rightstick != i.rightstick
            settings.python_command.keys.ser.ser.write((i.to_pokecon_str(ls, rs) + '\r\n').encode('utf-8'))
            prev = i
            time.sleep(i.seconds)
        settings.python_command.checkIfAlive()

@singledispatch
def send(iter: Iterable[GamepadInput | int | float]):
    c = Combo()
    c.parse(iter)
    c.send()

@send.register
def _send(*args: GamepadInput | int | float):
    send(args)
