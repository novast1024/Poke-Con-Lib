from typing import Final
from math import sin, cos, pi

from .input import GamepadInput, StickInput
from . import settings

# cached data
_UP_STICK_INPUT: Final[StickInput] = StickInput(y = -1.0)
_DOWN_STICK_INPUT: Final[StickInput] = StickInput(y = 1.0)
_LEFT_STICK_INPUT: Final[StickInput] = StickInput(x = -1.0)
_RIGHT_STICK_INPUT: Final[StickInput] = StickInput(x = 1.0)

def Up(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = _UP_STICK_INPUT)

def Down(seconds: float = 0.0) -> GamepadInput: 
    return GamepadInput(seconds or settings.input_seconds, rightstick = _DOWN_STICK_INPUT)

def Left(seconds: float = 0.0) -> GamepadInput: 
    return GamepadInput(seconds or settings.input_seconds, rightstick = _LEFT_STICK_INPUT)

def Right(seconds: float = 0.0) -> GamepadInput: 
    return GamepadInput(seconds or settings.input_seconds, rightstick = _RIGHT_STICK_INPUT)

# ==================== compass direction ==============================

def N(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = _UP_STICK_INPUT)

def NNE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 0.375), -sin(pi * 0.375)))

def NE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 0.25), -sin(pi * 0.25)))

def ENE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 0.125), -sin(pi * 0.125)))

def E(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = _RIGHT_STICK_INPUT)

def ESE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 1.875), -sin(pi * 1.875)))

def SE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 1.75), -sin(pi * 1.75)))

def SSE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 1.625), -sin(pi * 1.625)))

def S(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = _DOWN_STICK_INPUT)

def SSW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 1.375), -sin(pi * 1.375)))

def SW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 1.25), -sin(pi * 1.25)))

def WSW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 1.125), -sin(pi * 1.125)))

def W(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = _LEFT_STICK_INPUT)

def WNW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 0.875), -sin(pi * 0.875)))

def NW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 0.75), -sin(pi * 0.75)))

def NNW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, rightstick = StickInput(cos(pi * 0.625), -sin(pi * 0.625)))
