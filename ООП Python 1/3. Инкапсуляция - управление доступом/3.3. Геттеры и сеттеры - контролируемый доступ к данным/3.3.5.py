class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = 0
        self._age = self.set_age(age)

    def set_age(self, age):
        if 0 <= age <= 120:
            self._age = age

    def get_age(self):
        return self._age