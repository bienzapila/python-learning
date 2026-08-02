class SecureStorage:
    def __init__(self, name, max_weight, initial_weight, access_code):
        self.name = name
        self.max_weight = max_weight
        self._current_weight = 0
        self.set_current_weight(initial_weight)
        self.__access_code = 0
        self.set_access_code(access_code)

    def get_current_weight(self):
        return self._current_weight

    def set_current_weight(self, new_weight):
        if not isinstance(new_weight, int):
            print('Ошибка: вес должен быть целым числом')
        elif new_weight > self.max_weight:
            print('Ошибка: превышена вместимость хранилища')
        else:
            self._current_weight = new_weight
            print(f'Вес установлен: {self._current_weight}')

    def set_access_code(self, new_code):
        if not isinstance(new_code, int):
            print('Ошибка: код доступа должен быть целым числом')
        elif not 1000 <= new_code <= 9999:
            print('Ошибка: код доступа должен состоять из 4 цифр')
        else:
            self.__access_code = new_code
            print('Код доступа установлен')

    def __check_access_code(self, code):
        return code == self.__access_code

    def add_cargo(self, amount):
        if not isinstance(amount, int):
            print('Ошибка: вес груза должен быть целым числом')
        elif amount <= 0:
            print('Ошибка: вес груза должен быть положительным')
        elif self._current_weight + amount > self.max_weight:
            print('Ошибка: в хранилище недостаточно места')
        else:
            self._current_weight += amount
            print(f'Добавлено {amount} кг. Текущий вес: {self._current_weight} кг')

    def remove_cargo(self, amount, code):
        if not self.__check_access_code(code):
            print('Ошибка: неверный код доступа')
        elif not isinstance(amount, int):
            print('Ошибка: вес удаляемого груза должен быть целым числом')
        elif amount <= 0:
            print('Ошибка: вес удаляемого груза должен быть положительным')
        elif self._current_weight - amount < 0:
            print('Ошибка: в хранилище нет столько груза')
        else:
            self._current_weight -= amount
            print(f'Удалено {amount} кг. Текущий вес: {self._current_weight} кг')

    def change_access_code(self, old_code, new_code):
        if not old_code == self.__access_code:
            print('Ошибка: неверный текущий код доступа')
        else:
            self.set_access_code(new_code)

    def show_info(self):
        print(f'Хранилище: {self.name} | Груз: {self.get_current_weight()}/{self.max_weight} кг')


# Чтение входных данных

name = input().strip()

max_weight = int(input().strip())

initial_weight = int(input().strip())

initial_code = int(input().strip())

add_amount = int(input().strip())

remove_amount = int(input().strip())

entered_code = int(input().strip())

new_code = int(input().strip())

 

# Создание хранилища

storage = SecureStorage(name, max_weight, initial_weight, initial_code)

 

# Добавление груза

storage.add_cargo(add_amount)

 

# Попытка удалить груз

storage.remove_cargo(remove_amount, entered_code)

 

# Изменение кода доступа

storage.change_access_code(entered_code, new_code)

 

# Попытка удалить 1 кг с новым кодом

storage.remove_cargo(1, new_code)

 

# Попытка установить вес, превышающий вместимость на 1

storage.set_current_weight(max_weight + 1)

 

# Попытка установить вес строкой

storage.set_current_weight("много")

 

# Вывод итоговой информации

storage.show_info()