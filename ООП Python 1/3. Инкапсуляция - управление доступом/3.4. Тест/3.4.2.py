class SmartThermostat:
    def __init__(self, room_name, initial_temperature, service_code):
        self.room_name = room_name
        self._temperature = 20
        self.set_temperature(initial_temperature)
        self.__service_code = 0
        self.set_service_code(service_code)

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, new_temperature):
        if not isinstance(new_temperature, int):
            print('Ошибка: температура должна быть целым числом')
        elif not 5 <= new_temperature <= 35:
            print('Ошибка: температура должна быть от 5 до 35 градусов')
        else:
            self._temperature = new_temperature
            print(f'Температура установлена: {self._temperature}')

    def set_service_code(self, new_code):
        if not isinstance(new_code, int):
            print('Ошибка: сервисный код должен быть целым числом')
        elif not 1000 <= new_code <= 9999:
            print('Ошибка: сервисный код должен состоять из 4 цифр')
        else:
            self.__service_code = new_code
            print('Сервисный код установлен')

    def __check_service_code(self, code):
        return code == self.__service_code

    def increase_temperature(self, amount):
        if not isinstance(amount, int):
            print('Ошибка: значение повышения должно быть целым числом')
        elif amount <= 0:
            print('Ошибка: значение повышения должно быть положительным')
        elif self._temperature + amount > 35:
            print('Ошибка: температура не может быть выше 35 градусов')
        else:
            self._temperature += amount
            print(f'Температура повышена на {amount}. Текущая температура: {self._temperature}')

    def decrease_temperature(self, amount):
        if not isinstance(amount, int):
            print('Ошибка: значение понижения должно быть целым числом')
        elif amount <= 0:
            print('Ошибка: значение понижения должно быть положительным')
        elif self._temperature - amount < 5:
            print('Ошибка: температура не может быть ниже 5 градусов') 
        else:
            self._temperature -= amount
            print(f'Температура понижена на {amount}. Текущая температура: {self._temperature}')

    def set_temperature_by_code(self, new_temperature, code):
        if not self.__check_service_code(code):
            print('Ошибка: неверный сервисный код') 
        else:
            self.set_temperature(new_temperature)

    def change_service_code(self, old_code, new_code):
        if old_code != self.__service_code:
            print('Ошибка: неверный текущий сервисный код')
        else:
            self.set_service_code(new_code)

    def show_info(self):
        temp = self.get_temperature()
        print(f'Помещение: {self.room_name} | Температура: {temp} градусов')


room, temp, code = input(), int(input()), int(input())

thermostat = SmartThermostat(room, temp, code)

 

thermostat.increase_temperature(int(input()))

thermostat.set_temperature_by_code(int(input()), (input_code := int(input())))

thermostat.change_service_code(input_code, (new_code := int(input())))

thermostat.set_temperature_by_code(int(input()), new_code)

thermostat.decrease_temperature(2)

thermostat.set_temperature(-10)

thermostat.set_temperature("жарко")

thermostat.show_info()