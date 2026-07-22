class User:
    def __init__(self):
        self._age = 0

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if type(new_age) == int and new_age >= 0:
            self._age = new_age
        
    