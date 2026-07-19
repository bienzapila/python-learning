class Employee:
    company = 'Stepik'

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f'{self.name} работает в компании {Employee.company} на должности {self.position}.'