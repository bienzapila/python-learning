class GameCharacter:
    def __init__(self, name, max_health, initial_health, admin_code):
        self.name = name
        self.max_health = max_health
        self._health = 0
        self.set_health(initial_health)
        self.__admin_code = 0
        self.set_admin_code(admin_code)

    def get_health(self):
        return self._health

    def set_health(self, new_health):
        if not isinstance(new_health, int):
            print('Ошибка: здоровье должно быть целым числом')
        elif new_health > self.max_health:
            print('Ошибка: здоровье не может превышать максимальное')
        elif new_health < 0:
            print('Ошибка: здоровье не может быть отрицательным')
        else:
            self._health = new_health
            print(f'Здоровье установлено: {self._health}')

    def set_admin_code(self, new_code):
        if not isinstance(new_code, int):
            print('Ошибка: код администратора должен быть целым числом')
        elif not 1000 <= new_code <= 9999:
            print('Ошибка: код администратора должен состоять из 4 цифр')
        else:
            self.__admin_code = new_code
            print('Код администратора установлен')

    def __check_admin_code(self, code):
        return code == self.__admin_code

    def take_damage(self, amount):
        if not isinstance(amount, int):
            print('Ошибка: урон должен быть целым числом')
        elif amount <= 0:
            print('Ошибка: урон должен быть положительным')
        elif amount >= self._health:
            print('Ошибка: урон превышает текущее здоровье')
        else:
            self._health -= amount
            print(f'Получен урон: {amount}. Здоровье: {self._health}')

    def heal(self, amount):
        if not isinstance(amount, int):
            print('Ошибка: лечение должно быть целым числом')
        elif amount <= 0:
            print('Ошибка: лечение должно быть положительным')
        elif self._health + amount > self.max_health:
            print('Ошибка: здоровье превысит максимальное значение')
        else:
            self._health += amount
            print(f'Восстановлено здоровья: {amount}. Здоровье: {self._health}')

    def set_health_by_code(self, new_health, code):
        if not self.__check_admin_code(code):
            print('Ошибка: неверный код администратора')
        else:
            self.set_health(new_health)

    def change_admin_code(self, old_code, new_code):
        if not old_code == self.__admin_code:
            print('Ошибка: неверный текущий код администратора')
        else:
            self.set_admin_code(new_code)

    def show_info(self):
        print(f'Персонаж: {self.name} | Здоровье: {self.get_health()}/{self.max_health}')


name, max_health, initial_health, initial_code = input(), int(input()), int(input()), int(input())

character = GameCharacter(name, max_health, initial_health, initial_code)

 

character.take_damage(int(input()))

character.heal(int(input()))

character.set_health_by_code(int(input()), (entered_code := int(input())))

character.change_admin_code(entered_code, (new_code := int(input())))

character.set_health_by_code(int(input()), new_code)

character.set_health(-10)

character.set_health("много")

character.show_info()