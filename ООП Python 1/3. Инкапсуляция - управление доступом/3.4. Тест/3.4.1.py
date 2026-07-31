class SecureWallet:
    def __init__(self, name, initial_balance, pin):
        self.name = name

        self._balance = 0
        self.set_balance(initial_balance)

        self.__pin = 0
        self.set_pin(pin)

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if not isinstance(new_balance, int):
            print('Ошибка: баланс должен быть целым числом')
        elif new_balance < 0:
            print('Ошибка: баланс не может быть отрицательным')
        else:
            self._balance = new_balance
            print(f'Баланс установлен: {self._balance}')

    def set_pin(self, new_pin):
        if not isinstance(new_pin, int):
            print('Ошибка: PIN-код должен быть целым числом')
        elif not 1000 <= new_pin <= 9999:
            print('Ошибка: PIN-код должен состоять из 4 цифр')
        else:
            self.__pin = new_pin
            print('PIN-код установлен')

    def __check_pin(self, pin):
        return pin == self.__pin

    def deposit(self, amount):
        if not isinstance(amount, int):
            print('Ошибка: сумма пополнения должна быть целым числом')
        elif amount <= 0:
            print('Ошибка: сумма пополнения должна быть положительной')
        else:
            self._balance += amount
            print(f'Кошелек пополнен на {amount}. Баланс: {self._balance}')

    def withdraw(self, amount, pin):
        if not self.__check_pin(pin):
            print('Ошибка: неверный PIN-код')
        elif not isinstance(amount, int):
            print('Ошибка: сумма снятия должна быть целым числом')
        elif amount <= 0:
            print('Ошибка: сумма снятия должна быть положительной')
        elif amount > self._balance:
            print('Ошибка: недостаточно средств')
        else:
            self._balance -= amount
            print(f'Снято {amount}. Баланс: {self._balance}')

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            print('Ошибка: неверный текущий PIN-код')
        else:
            self.set_pin(new_pin)

    def show_info(self):
        bal = self.get_balance()
        print(f'Владелец: {self.name} | Баланс: {bal}')


name = input()
in_balance = int(input())
in_pin = int(input())

d_amount = int(input())
w_amount = int(input())

w_pin = int(input())
n_pin = int(input())


wallet = SecureWallet(name, in_balance, in_pin)
wallet.deposit(d_amount)
wallet.withdraw(w_amount, w_pin)
wallet.change_pin(w_pin, n_pin)
wallet.withdraw(1, n_pin)
wallet.set_balance(-1000)
wallet.set_balance('gh')
wallet.show_info()    