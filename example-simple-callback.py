import threesixty
import json

def a_callback(controller):
    print "You're pressing the 'A' button"

def guide_callback(controller):
    print "current state: " + json.dumps(controller.get(), indent=4)
    return False # stop propagating the event until it's False again

controllers = threesixty.controllers() # get all controllers
print "Controller count:", len(controllers)

if len(controllers) > 0:
    c = controllers[0]

    c.on(threesixty.A, a_callback) # add a callback for the A button
    c.on(threesixty.GUIDE, guide_callback) # add a callback for the GUIDE (big (X) in the middle of the controller)
