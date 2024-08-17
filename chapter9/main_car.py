import os

# from car import Car
from car import ElectricCar, Car

os.system("clear")

my_new_car = Car('audi', 'a4', 2024)

print(my_new_car.describe())
my_new_car.read_odometer()
print(my_new_car.make)
my_new_car.make = "BMW"
print(my_new_car.make)
my_new_car.fill_gas_tank()
my_new_car.odometer = 147
my_new_car.read_odometer()
my_new_car.odometer = 100_000
my_new_car.odometer = 230
my_new_car.read_odometer()
my_new_car.increment_odometer(300)
my_new_car.read_odometer()
print("\n")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.describe())
my_leaf.make = "Tesla"
print(my_leaf.describe())
my_leaf.fill_gas_tank()
my_leaf.read_odometer()
my_leaf.odometer = 230
my_leaf.read_odometer()
my_leaf.increment_odometer(300)
my_leaf.read_odometer()
my_leaf.battery.describe_batery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()



