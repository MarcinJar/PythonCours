import os

from group_car_restaurant import Car, Restaurant

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

pilushRestaurant = Restaurant("Swojska Chata", "pierogarnia")
pilushRestaurant.describe()
pilushRestaurant.number_served = 10
pilushRestaurant.show_number_served_clients()
pilushRestaurant.increment_number_served(4)
pilushRestaurant.show_number_served_clients()
pilushRestaurant.increment_number_served(1)
pilushRestaurant.show_number_served_clients()