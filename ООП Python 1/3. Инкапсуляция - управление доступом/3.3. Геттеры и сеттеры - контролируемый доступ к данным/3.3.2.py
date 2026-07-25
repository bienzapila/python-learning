class Device:
    def __init__(self):
        self._voltage = 0

    def set_voltage(self, voltage):
        self._voltage = voltage

    def get_voltage(self):
        return self._voltage