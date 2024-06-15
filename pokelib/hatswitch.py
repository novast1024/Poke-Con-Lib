from typing import Final

from .input import GamepadInput, HatSwitchInput
from . import settings

# cached data
_UP_HAT_SWITCH_INPUT: Final[HatSwitchInput] = HatSwitchInput(0b0001)
_RIGHT_HAT_SWITCH_INPUT: Final[HatSwitchInput] = HatSwitchInput(0b0010)
_DOWN_HAT_SWITCH_INPUT: Final[HatSwitchInput] = HatSwitchInput(0b0100)
_LEFT_HAT_SWITCH_INPUT: Final[HatSwitchInput] = HatSwitchInput(0b1000)

def Up(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _UP_HAT_SWITCH_INPUT)

def Right(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _RIGHT_HAT_SWITCH_INPUT)

def Down(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _DOWN_HAT_SWITCH_INPUT)

def Left(seconds: float = 0.0) -> GamepadInput: 
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _LEFT_HAT_SWITCH_INPUT)

# ==================== compass direction ==============================

# cached data
_N_HAT_SWITCH_INPUT: Final[HatSwitchInput] = _UP_HAT_SWITCH_INPUT
_E_HAT_SWITCH_INPUT: Final[HatSwitchInput] = _RIGHT_HAT_SWITCH_INPUT
_S_HAT_SWITCH_INPUT: Final[HatSwitchInput] = _DOWN_HAT_SWITCH_INPUT
_W_HAT_SWITCH_INPUT: Final[HatSwitchInput] = _LEFT_HAT_SWITCH_INPUT

_NE_HAT_SWITCH_INPUT: Final[HatSwitchInput] = _N_HAT_SWITCH_INPUT + _E_HAT_SWITCH_INPUT
_SE_HAT_SWITCH_INPUT: Final[HatSwitchInput] = _S_HAT_SWITCH_INPUT + _E_HAT_SWITCH_INPUT
_SW_HAT_SWITCH_INPUT: Final[HatSwitchInput] = _S_HAT_SWITCH_INPUT + _W_HAT_SWITCH_INPUT
_NW_HAT_SWITCH_INPUT: Final[HatSwitchInput] = _N_HAT_SWITCH_INPUT + _W_HAT_SWITCH_INPUT

def N(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _N_HAT_SWITCH_INPUT)

def NE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _NE_HAT_SWITCH_INPUT)

def E(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _E_HAT_SWITCH_INPUT)

def SE(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _SE_HAT_SWITCH_INPUT)

def S(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _S_HAT_SWITCH_INPUT)

def SW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _SW_HAT_SWITCH_INPUT)

def W(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _W_HAT_SWITCH_INPUT)

def NW(seconds: float = 0.0) -> GamepadInput:
    return GamepadInput(seconds or settings.input_seconds, hatswitch = _NW_HAT_SWITCH_INPUT)
