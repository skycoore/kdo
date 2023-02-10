import inspect

if "listeners" not in globals():
    global listeners
    listeners = {}

def addEventListener(event, listener):
    listeners[event.__code__] = listener

def fire():
    event = inspect.currentframe().f_back.f_code
    if event in listeners:
        return listeners[event]()