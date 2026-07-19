class Character:
    character_count = 0
    
    def __init__(self, name):
        self.name = name
        Character.character_count += 1