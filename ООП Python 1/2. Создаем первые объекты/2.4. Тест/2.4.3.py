class CourierRobot:
    service_name = "Python Delivery"
    total_robots = 0

    def __init__(self, name, max_energy):
        self.name = name
        self.max_energy = max_energy
        self.current_energy = 0
        self.delivered_orders = 0

        CourierRobot.total_robots += 1

    def charge(self, amount):
        if self.current_energy + amount <= self.max_energy:
            print(f'{self.name}: получено {amount} ед. энергии')
            self.current_energy += amount
        else:
            print(f'{self.name}: аккумулятор переполнен')

    def deliver(self, energy_cost):
        if energy_cost <= self.current_energy:
            self.current_energy -= energy_cost
            self.delivered_orders += 1
            print(f'{self.name}: заказ доставлен, потрачено {energy_cost} ед. энергии')
        else:
            print(f'{self.name}: недостаточно энергии')

    def show_info(self):
        print(f'Робот {self.name} | Служба: {self.service_name} | Энергия: {self.current_energy}/{self.max_energy} | Заказов: {self.delivered_orders}')

    def set_personal_service(self, service_name):
        self.service_name = service_name


name1 = input()
max_energy1 = int(input())

name2 = input()
max_energy2 = int(input())

amount1 = int(input())
amount2 = int(input())

cost1 = int(input())
cost2 = int(input())

service_name_new = input()
service_name_personal = input()


robot1 = CourierRobot(name1, max_energy1)
robot2 = CourierRobot(name2, max_energy2)

robot1.charge(amount1)
robot2.charge(amount2)

CourierRobot.service_name = service_name_new
robot1.set_personal_service(service_name_personal)

robot1.deliver(cost1)
robot2.deliver(cost2)

robot1.show_info()
robot2.show_info()

print(f'Всего роботов: {CourierRobot.total_robots}')