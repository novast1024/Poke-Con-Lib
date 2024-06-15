from typing import Final

from .input import GamepadInput, ButtonInput
from . import settings

# cached data
_Y_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x01)
_B_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x02)
_A_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x04)
_X_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x08)
_L_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x10)
_R_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x20)
_ZL_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x40)
_ZR_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x80)
_MINUS_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x0100)
_PLUS_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x0200)
_LS_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x0400)
_RS_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x0800)
_HOME_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x1000)
_CAPTURE_BUTTON_INPUT: Final[ButtonInput] = ButtonInput(0x2000)


def Y(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _Y_BUTTON_INPUT)

def B(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _B_BUTTON_INPUT)

def A(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _A_BUTTON_INPUT)

def X(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _X_BUTTON_INPUT)

def L(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _L_BUTTON_INPUT)

def R(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _R_BUTTON_INPUT)

def ZL(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _ZL_BUTTON_INPUT)

def ZR(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _ZR_BUTTON_INPUT)

def Minus(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _MINUS_BUTTON_INPUT)

def Plus(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _PLUS_BUTTON_INPUT)

def LS(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _LS_BUTTON_INPUT)

def RS(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _RS_BUTTON_INPUT)

def Home(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, button = _HOME_BUTTON_INPUT)

def Capture(seconds: float = 0.0) -> GamepadInput: 
    return GamepadInput(seconds or settings.input_seconds, button = _CAPTURE_BUTTON_INPUT)
