import xinput
from .. import icontroller
from .. import constants
from .. import events


class Controller(icontroller.IController):
    def __init__(self,  device):
        self.__device = device
        self.eventhandlers = {}
        
        self.get()

        self.__updater = events.ControllerUpdater(self)
        self.__updater.start()

    def __mask(self, number, i):
        """Masks a given number  at the i-th bit"""
        return number & (1 << i) != 0

    def __enumerate_buttons(self, buttons):
        """Converts the button-result into a human-readable dictionary"""
        button_config = {
            constants.A: self.__mask(buttons, 12),
            constants.B: self.__mask(buttons, 13),
            constants.X: self.__mask(buttons, 14),
            constants.Y: self.__mask(buttons, 15)
        }

        button_config[constants.MSLP] = self.__mask(buttons, 6)
        button_config[constants.MSRP] = self.__mask(buttons, 7)

        button_config[constants.LB] = self.__mask(buttons, 8)
        button_config[constants.RB] = self.__mask(buttons, 9)

        button_config[constants.START] = self.__mask(buttons, 4)
        button_config[constants.BACK] = self.__mask(buttons, 5)
        button_config[constants.GUIDE] = self.__mask(buttons, 10)

        button_config[constants.UP] = self.__mask(buttons, 0)
        button_config[constants.DOWN] = self.__mask(buttons, 1)
        button_config[constants.LEFT] = self.__mask(buttons, 2)
        button_config[constants.RIGHT] = self.__mask(buttons, 3)

        return button_config

    def __eval_ministick(self, x, y):
        """Corrects the ministick's position with a dead-zone of 0.25"""
        max_stick_position = 32768.0
        
        x /= max_stick_position
        y /= max_stick_position
        magnitude = pow(pow(x, 2) + pow(y, 2), 0.5)
        
        if magnitude < 0.25:
            x = y = 0

        return (x, y)

    def __enumerate_battery(self, battery):
        """Converts the given battery struct to a human-readable form"""
        battery_type  = battery.BatteryType
        battery_level = battery.BatteryLevel

        if battery_type == 0:
            battery_type = constants.BATTERY_TYPE_DISCONNECTED
        elif battery_type == 1:
            battery_type = constants.BATTERY_TYPE_WIRED
        elif battery_type == 2:
            battery_type = constants.BATTERY_TYPE_ALKALINE
        elif battery_type == 3:
            battery_type = constants.BATTERY_TYPE_NIMH
        else:
            battery_type = constants.BATTERY_TYPE_UNKNOWN

        if battery_level == 0:
            battery_level = constants.BATTERY_LEVEL_EMPTY
        elif battery_level == 1:
            battery_level = constants.BATTERY_LEVEL_LOW
        elif battery_level == 2:
            battery_level = constants.BATTERY_LEVEL_MEDIUM
        else: 
            battery_level = constants.BATTERY_LEVEL_FULL

        return (battery_type, battery_level)

    def get(self):
        error, state = xinput.XInputGetState(self.__device)
        

        if error == 1167:
            raise Exception("Device cannot be found at {%d}"%self.__device)
        elif not error:
            gamepad = state.gamepad
            data = self.__enumerate_buttons(gamepad.buttons)

            data[constants.LT] = gamepad.left_trigger / 255.0
            data[constants.RT] = gamepad.right_trigger / 255.0

            data[constants.MSL] = self.__eval_ministick(gamepad.l_thumb_x, gamepad.l_thumb_y)
            data[constants.MSR] = self.__eval_ministick(gamepad.r_thumb_x, gamepad.r_thumb_y)

            battery = xinput.XInputGetBatteryInformation(self.__device, 0)
            data[constants.BATTERY_TYPE], data[constants.BATTERY_LEVEL] = self.__enumerate_battery(battery)

            return data

    def on(self, event, action):
        if event == None:
            event = "ALWAYS"
        
        if not event in self.eventhandlers.keys():
            self.eventhandlers[event] = []

        self.eventhandlers[event].append(action)

    def vibrate(self, left, right):
        vibration = xinput.XINPUT_VIBRATION(int(left * 65535), int(right * 65535))
        xinput.XInputSetState(self.__device, vibration)
