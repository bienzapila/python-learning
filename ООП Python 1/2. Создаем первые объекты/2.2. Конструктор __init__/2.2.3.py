class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        
    def get_info(self):
        return f'Имя: {self.username}, Возраст: {self.age}'
