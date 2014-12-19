import platform
import icontroller
from constants import *

system = platform.system()

if system == "Windows":
    from windows.control import *

def controllers():
    devices = []
    
    for i in range(4):
        try:
            devices.append(Controller(i))
        except:
            pass

    return devices
