import ctypes
import structs

try:
    xinput = ctypes.windll.xinput1_3
except:
    raise Exception("Unable to detect xinput.dll")


GetProcAddress = ctypes.windll.kernel32.GetProcAddress
__XInputGetState_addr = GetProcAddress(xinput._handle, ctypes.c_char_p(100))
__XInputGetState_proto = ctypes.WINFUNCTYPE(ctypes.c_uint)
_XInputGetState = __XInputGetState_proto(__XInputGetState_addr)
_XInputGetState.argtypes = [ctypes.c_uint, ctypes.POINTER(structs.XINPUT_STATE)]
_XInputGetState.restype = ctypes.c_uint

def XInputGetState(device):
    state = structs.XINPUT_STATE()
    error = _XInputGetState(device, ctypes.byref(state))

    return (error, state)


_XInputSetState = xinput.XInputSetState
_XInputSetState.argtypes = [ctypes.c_uint, ctypes.POINTER(structs.XINPUT_VIBRATION)]
_XInputSetState.restype = ctypes.c_uint

XINPUT_VIBRATION = structs.XINPUT_VIBRATION

def XInputSetState(device, vibration):
    _XInputSetState(device, ctypes.byref(vibration))


_XInputGetBatteryInformation = xinput.XInputGetBatteryInformation
_XInputGetBatteryInformation.argtypes = [ctypes.c_uint, ctypes.c_byte, ctypes.POINTER(structs.XINPUT_BATTERY_INFORMATION)]
_XInputGetBatteryInformation.restype = ctypes.c_uint

def XInputGetBatteryInformation(user_index, device):
    battery = structs.XINPUT_BATTERY_INFORMATION()
    error = _XInputGetBatteryInformation(user_index, device, ctypes.byref(battery))

    return battery
