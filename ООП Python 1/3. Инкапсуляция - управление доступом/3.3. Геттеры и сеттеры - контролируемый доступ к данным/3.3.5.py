class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = 0
        self.set_age(age)

    def set_age(self, new_age):
        if 0 <= new_age <= 120 and isinstance(new_age, int):
            self._age = new_age

    def get_age(self):
        return self._age