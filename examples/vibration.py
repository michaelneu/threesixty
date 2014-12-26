import threesixty

controllers = threesixty.controllers() # get all controllers

def always_callback(controller):
    """Vibrates the controller according to the right ministick (msr).
    position_msr = right --> right motor
    position_msr = left --> left motor"""

    state = controller.get() # get the current state
    ministick_r = state[threesixty.MSR] # get the ministicks value
    x_value = ministick_r[0] # get the x-value

    if x_value < 0:
        controller.vibrate(-x_value, 0) # only vibrate using the left motor
    elif x_value > 0:
        controller.vibrate(0, x_value) # only vibrate using the right motor
    else:
        controller.vibrate(0, 0) # reset vibration if stick isn't pushed

if len(controllers) > 0:
    c = controllers[0] # get the first controller
    c.on(None, always_callback) # add an always triggering callback
