import ctypes

# https://github.com/r4dian/Xbox-360-Controller-for-Python/blob/master/xinput.py
# http://pydoc.net/Python/jaraco.input/1.0.1/jaraco.input.linux2.joystick/

class XINPUT_GAMEPAD(ctypes.Structure):
    _fields_ = [
        ('buttons', ctypes.c_ushort),
        ('left_trigger', ctypes.c_ubyte),
        ('right_trigger', ctypes.c_ubyte),
        ('l_thumb_x', ctypes.c_short),
        ('l_thumb_y', ctypes.c_short),
        ('r_thumb_x', ctypes.c_short),
        ('r_thumb_y', ctypes.c_short)
    ]

class XINPUT_VIBRATION(ctypes.Structure):
    _fields_ = [("wLeftMotorSpeed", ctypes.c_ushort),
                ("wRightMotorSpeed", ctypes.c_ushort)]

class XINPUT_STATE(ctypes.Structure):
    _fields_ = [
        ('packet_number', ctypes.c_ulong),
        ('gamepad', XINPUT_GAMEPAD),
    ]
