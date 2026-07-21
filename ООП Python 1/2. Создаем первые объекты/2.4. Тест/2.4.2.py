class SpaceShip():
    agency = "Python Space"
    total_ships = 0
    def __init__(self, name, max_fuel, current_fuel=0):
        self.name = name
        self.max_fuel = max_fuel
        self.current_fuel = current_fuel
        SpaceShip.total_ships += 1
    
    def refuel(self, amount):
        if self.current_fuel + amount <= self.max_fuel:
            print(f'{self.name}: заправлено {amount} ед. топлива')
            self.current_fuel += amount
        else:
            print(f'{self.name}: топливный бак переполнен')

    def fly(self, fuel_cost):
        if fuel_cost <= self.current_fuel:
            print(f'{self.name}: полет выполнен, потрачено {fuel_cost} ед. топлива')
            self.current_fuel -= fuel_cost
        else:
            print(f'{self.name}: недостаточно топлива')

    def show_info(self):
        print(f'Корабль {self.name} | Агентство: {self.agency} | Топливо: {self.current_fuel}/{self.max_fuel}')
    
    def set_personal_agency(self, agency):
        self.agency = agency

name1 = input()
max_fuel1 = int(input())
name2 = input()
max_fuel2 = int(input())
fuel1 = int(input())
fuel2 = int(input())
cost1 = int(input())
cost2 = int(input())
agency_new = input()
agency1 = input()

ship1, ship2 = SpaceShip(name1, max_fuel1), SpaceShip(name2, max_fuel2)

ship1.refuel(fuel1), ship2.refuel(fuel2)

SpaceShip.agency = agency_new

ship1.set_personal_agency(agency1)

ship1.fly(cost1), ship2.fly(cost2)

ship1.show_info()
ship2.show_info()

print(f'Всего кораблей: {SpaceShip.total_ships}')
