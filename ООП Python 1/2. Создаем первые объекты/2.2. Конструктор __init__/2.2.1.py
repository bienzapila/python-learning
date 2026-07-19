class Cat:
    def __init__(self):
        self.state = 'спит'
    def get_state(self):
        return self.state
    
cat = Cat()
print(cat.get_state())