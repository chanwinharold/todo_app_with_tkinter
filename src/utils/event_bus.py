class EventBus:
    _instance = None
    _callbacks = {}

    def __init__(self):
        if EventBus._instance is not None:
            raise Exception("EventBus is a singleton, use EventBus.insance()")
        EventBus._callbacks = {}

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def inscrire(self, event_name: str, callback):
        if event_name not in self._callbacks:
            self._callbacks[event_name] = []
        if callback not in self._callbacks[event_name]:
            self._callbacks[event_name].append(callback)

    def desinscrire(self, event_name: str, callback=None):
        if callback is None:
            self._callbacks.pop(event_name, None)
        elif event_name in self._callbacks:
            self._callbacks[event_name] = [c for c in self._callbacks[event_name] if c != callback]

    def emet(self, event_name: str, data=None):
        if event_name in self._callbacks:
            for callback in self._callbacks[event_name]:
                try:
                    callback(data)
                except Exception as e:
                    print(f"Error in event callback for {event_name}: {e}")


event_bus = EventBus.instance()