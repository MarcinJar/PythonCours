import os

from restaurant import Restaurant, IceCreamStand

os.system("clear")

sushRestaurant = Restaurant("Tokyo", "sushi")
italyRestaurant = Restaurant("Roma", "pizzeria")
pilushRestaurant = Restaurant("Swojska Chata", "pierogarnia")

sushRestaurant.describe()
italyRestaurant.describe()
pilushRestaurant.describe()

sushRestaurant.number_served = 10
sushRestaurant.show_number_served_clients()
sushRestaurant.increment_number_served(4)
sushRestaurant.show_number_served_clients()
sushRestaurant.increment_number_served(1)
sushRestaurant.show_number_served_clients()
print("\n")

iceCreamRestaurant = IceCreamStand("Lodziarnia", "mrożonki", 3)
iceCreamRestaurant.describe()
iceCreamRestaurant.increment_number_served(3)
iceCreamRestaurant.show_number_served_clients()
iceCreamRestaurant.show_flavors()
iceCreamRestaurant.add_flavors()
iceCreamRestaurant.increment_number_served(5)
iceCreamRestaurant.show_number_served_clients()
iceCreamRestaurant.show_flavors()
iceCreamRestaurant.add_flavors()
iceCreamRestaurant.increment_number_served(1)
iceCreamRestaurant.show_number_served_clients()
iceCreamRestaurant.show_flavors()