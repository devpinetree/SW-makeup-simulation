import adsk.core, adsk.fusion, adsk.cam, traceback, Leap

# Globals
_app = adsk.core.Application.cast(None)
_ui = adsk.core.UserInterface.cast(None)
_leap_controller = adsk.core.Application.cast(None)


class SampleListener(Leap.Listener):
    def on_init(self, controller):
        print ("Initialized")

    def on_connect(self, controller):
        print ("Connected")

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print ("Disconnected")

    def on_exit(self, controller):
        print ("Exited")


def run(context):
    ui = None
    try:
        global _app, _ui
        _app = adsk.core.Application.get()
        _ui  = _app.userInterface
        _ui.messageBox('Hello addin')

        # Create a sample listener and controller
        global _leap_controller
        listener = SampleListener()
        _leap_controller = Leap.Controller()

        # Have the sample listener receive events from the controller
        _leap_controller.add_listener(listener)  
    except:
        if _ui:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    global _ui
    _ui = None
    try:
        _app = adsk.core.Application.get()
        _ui  = _app.userInterface
        _ui.messageBox('Stop addin')

    except:
        if _ui:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
