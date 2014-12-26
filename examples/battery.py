import threesixty

def guide_callback(controller):
    state = controller.get()
    battery_type = state[threesixty.BATTERY_TYPE]
    battery_level = state[threesixty.BATTERY_LEVEL]
    
    print "The controller's battery is a '%s'"%battery_type
    print "The level of this battery is '%s'\n"%battery_level

    return False

controllers = threesixty.controllers()
print "Controller count:", len(controllers)

if len(controllers) > 0:
    c = controllers[0]

    c.on(threesixty.GUIDE, guide_callback)
