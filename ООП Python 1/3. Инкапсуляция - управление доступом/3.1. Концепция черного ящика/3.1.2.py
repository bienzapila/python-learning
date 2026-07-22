class LightSwitch:
    def __init__(self):
        self._is_on = False

    def toggle(self):
        self._is_on = not self._is_on

    def is_on(self):
        return self._is_on