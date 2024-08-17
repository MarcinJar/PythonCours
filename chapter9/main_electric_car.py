import os

from car import ElectricCar

os.system("clear")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.describe())
my_leaf.fill_gas_tank()
my_leaf.battery.describe_batery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()