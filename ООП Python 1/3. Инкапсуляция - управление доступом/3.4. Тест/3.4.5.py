class SecurePrinter:
    def __init__(self, name, max_paper, initial_paper, service_code):
        self.name = name
        self.max_paper = max_paper

        self._paper_count = 0
        self.set_paper_count(initial_paper)

        self.__service_code = 0
        self.set_service_code(service_code)

    def get_paper_count(self):
        return self._paper_count

    def set_paper_count(self, new_count):
        if not isinstance(new_count, int):
            print('Ошибка: количество бумаги должно быть целым числом')
        elif new_count < 0:
            print('Ошибка: количество бумаги не может быть отрицательным')
        elif new_count > self.max_paper:
            print('Ошибка: превышена вместимость лотка')
        else:
            self._paper_count = new_count
            print(f'Количество бумаги установлено: {self._paper_count}')

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

    def add_paper(self, amount):
        if not isinstance(amount, int):
            print('Ошибка: количество добавляемой бумаги должно быть целым числом')
        elif amount <= 0:
            print('Ошибка: количество добавляемой бумаги должно быть положительным')
        elif amount + self._paper_count > self.max_paper:
            print('Ошибка: в лотке недостаточно места')
        else:
            self._paper_count += amount
            print(f'Добавлено бумаги: {amount}. В лотке: {self._paper_count}')

    def print_pages(self, pages):
        if not isinstance(pages, int):
            print('Ошибка: количество страниц должно быть целым числом')
        elif pages <= 0:
            print('Ошибка: количество страниц должно быть положительным')
        elif pages > self._paper_count:
            print('Ошибка: недостаточно бумаги')
        else:
            self._paper_count -= pages
            print(f'Напечатано страниц: {pages}. Осталось бумаги: {self._paper_count}')

    def set_paper_by_code(self, new_count, code):
        if not self.__check_service_code(code):
            print('Ошибка: неверный сервисный код')
        else:
            self.set_paper_count(new_count)

    def change_service_code(self, old_code, new_code):
        if not old_code == self.__service_code:
            print('Ошибка: неверный текущий сервисный код')
        else:
            self.set_service_code(new_code)

    def show_info(self):
        print(f'Принтер: {self.name} | Бумага: {self.get_paper_count()}/{self.max_paper}')


name, max_paper, initial_paper, initial_code = input(), int(input()), int(input()), int(input())

printer = SecurePrinter(name, max_paper, initial_paper, initial_code)

 

printer.add_paper(int(input()))

printer.print_pages(int(input()))

printer.set_paper_by_code(int(input()), (entered_code := int(input())))

printer.change_service_code(entered_code, (new_code := int(input())))

printer.set_paper_by_code(int(input()), new_code)

printer.set_paper_count(-1)

printer.set_paper_count("много")

printer.show_info()