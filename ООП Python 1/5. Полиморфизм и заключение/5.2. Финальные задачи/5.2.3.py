class Character:
    def __init__(self, name, damage):
        self.name = name
        self._damage = damage
        self._health = 100
    def attack(self, target):
        target.take_damage(self._damage)
    def take_damage(self, amount):
        self._health -= amount
    def get_status(self):
        return f"Имя: {self.name}, Здоровье: {self._health}"

class Warrior(Character):
    def __init__(self, name, damage, armor):
        super().__init__(name, damage)
        self.armor = armor
    def take_damage(self, amount):
        new_amount = amount - self.armor
        self._health -=  new_amount if new_amount > 0 else 0

class Mage(Character):
    def __init__(self, name, damage, mana):
        super().__init__(name, damage)
        self.mana = mana
    def attack(self, target):
        if self.mana >= 10:
            self.mana -= 10
            super().attack(target)