class Thermostat:
    def __init__(self, temp):
        self._temperature = temp

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, new_temp):
        if 0 <= new_temp <= 100:
            self._temperature = new_temp