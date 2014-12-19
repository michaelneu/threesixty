import threading
import time

class ControllerUpdater(threading.Thread):
    def __init__(self, controller, interval=25):
        """Calls the controller's update-callbacks in <interval> milliseconds"""
        threading.Thread.__init__(self, target=self.do_work, args=())
        self.__controller = controller
        self.__update_interval = interval
        self.daemon = True

    def do_work(self):
        """The background-method"""
        handlersHandled = {}
        running_handlers = {}
        
        while True:
            state = self.__controller.get()
            handlers = self.__controller.eventhandlers

            for handler in running_handlers.keys():
                runner = running_handlers[handler]
                
                if runner.done_handling != None:
                    running_handlers.pop(handler)
                    
                    if runner.done_handling:
                        handlersHandled[runner.event].append(handler)
            
            for event in handlers.keys():
                if not event in handlersHandled.keys():
                    handlersHandled[event] = []
                
                if event == "ALWAYS" or state[event]:
                    for handler in handlers[event]:
                        if (handler not in handlersHandled[event]) and (handler not in running_handlers.keys()):
                            runner = HandlerRunner(handler, self.__controller, event)
                            runner.start()

                            running_handlers[handler] = runner
                else:
                    handlersHandled[event] = []
            
            time.sleep(self.__update_interval / 1000.0)

class HandlerRunner(threading.Thread):
    def __init__(self, handler, controller, event):
        """Executes the controller's handler in the background"""
        threading.Thread.__init__(self, target=self.do_work, args=())
        self.__controller = controller
        self.handler = handler
        self.event = event
        self.done_handling = None
        self.daemon = True

    def do_work(self):
        """The background-execution"""
        self.done_handling = self.handler(self.__controller) == False
