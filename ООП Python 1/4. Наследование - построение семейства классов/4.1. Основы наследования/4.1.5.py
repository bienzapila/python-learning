class Worker:
    def __init__(self, name, position):
        self._name = name
        self._position = position

class HRManager(Worker):
    def get_employee_info(self):
        return f'Имя: {self._name}, Должность: {self._position}'
    