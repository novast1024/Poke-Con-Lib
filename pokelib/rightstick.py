from typing import Final

from .input import GamepadInput, StickInput
from . import default

# cached data
_UP_STICK_INPUT: Final[StickInput] = StickInput(y = -1.0)
_DOWN_STICK_INPUT: Final[StickInput] = StickInput(y = 1.0)
_LEFT_STICK_INPUT: Final[StickInput] = StickInput(x = -1.0)
_RIGHT_STICK_INPUT: Final[StickInput] = StickInput(x = 1.0)

def Up(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _UP_STICK_INPUT)

def Down(seconds: float = 0.0) -> GamepadInput: 
    return GamepadInput(seconds or default.input_seconds, rightstick = _DOWN_STICK_INPUT)

def Left(seconds: float = 0.0) -> GamepadInput: 
    return GamepadInput(seconds or default.input_seconds, rightstick = _LEFT_STICK_INPUT)

def Right(seconds: float = 0.0) -> GamepadInput: 
    return GamepadInput(seconds or default.input_seconds, rightstick = _RIGHT_STICK_INPUT)

# ==================== compass direction ==============================

# cached data
_N_STICK_INPUT: Final[StickInput] = _UP_STICK_INPUT
_E_STICK_INPUT: Final[StickInput] = _RIGHT_STICK_INPUT
_S_STICK_INPUT: Final[StickInput] = _DOWN_STICK_INPUT
_W_STICK_INPUT: Final[StickInput] = _LEFT_STICK_INPUT

_NE_STICK_INPUT: Final[StickInput] = _N_STICK_INPUT + _E_STICK_INPUT
_SE_STICK_INPUT: Final[StickInput] = _S_STICK_INPUT + _E_STICK_INPUT
_SW_STICK_INPUT: Final[StickInput] = _S_STICK_INPUT + _W_STICK_INPUT
_NW_STICK_INPUT: Final[StickInput] = _N_STICK_INPUT + _W_STICK_INPUT

_NNE_STICK_INPUT: Final[StickInput] = _N_STICK_INPUT + _NE_STICK_INPUT
_ENE_STICK_INPUT: Final[StickInput] = _E_STICK_INPUT + _NE_STICK_INPUT
_ESE_STICK_INPUT: Final[StickInput] = _E_STICK_INPUT + _SE_STICK_INPUT
_SSE_STICK_INPUT: Final[StickInput] = _S_STICK_INPUT + _SE_STICK_INPUT
_SSW_STICK_INPUT: Final[StickInput] = _S_STICK_INPUT + _SW_STICK_INPUT
_WSW_STICK_INPUT: Final[StickInput] = _W_STICK_INPUT + _SW_STICK_INPUT
_WNW_STICK_INPUT: Final[StickInput] = _W_STICK_INPUT + _NW_STICK_INPUT
_NNW_STICK_INPUT: Final[StickInput] = _N_STICK_INPUT + _NW_STICK_INPUT

def N(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _N_STICK_INPUT)

def NNE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _NNE_STICK_INPUT)

def NE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _NE_STICK_INPUT)

def ENE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _ENE_STICK_INPUT)

def E(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _E_STICK_INPUT)

def ESE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _ESE_STICK_INPUT)

def SE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _SE_STICK_INPUT)

def SSE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _SSE_STICK_INPUT)

def S(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _S_STICK_INPUT)

def SSW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _SSW_STICK_INPUT)

def SW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _SW_STICK_INPUT)

def WSW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _WSW_STICK_INPUT)

def W(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _W_STICK_INPUT)

def WNW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _WNW_STICK_INPUT)

def NW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _NW_STICK_INPUT)

def NNW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or default.input_seconds, rightstick = _NNW_STICK_INPUT)
