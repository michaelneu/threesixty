class IController(object):
    def __init__(self, device):
        """Initializes a new Controller-object"""
        raise NotImplementedError()
    
    def on(self, event, function):
        """Adds an eventhandler for given event"""
        raise NotImplementedError()
    
    def get(self):
        """Returns the current state of the controller"""
        raise NotImplementedError()

    def vibrate(self, left, right):
        """Sets the controllers vibration"""
        raise NotImplementedError()
