import os

os.system("clear")

class Restaurant:
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type
        self.__number_served = 0

    @property
    def number_served (self):
        return self.__number_served      

    @number_served .setter
    def number_served (self, value):
        if value >= 0:
            self.__number_served = value
        else:
            print(f"Nie można obsłużyć mniej niż 0 klientów!")

    def increment_number_served (self, value):
        if value >= 0:
            self.__number_served += value
        else:
            print(f"Nie można obsłużyć ujemnej wartości klientów klientów!")

    def describe(self) -> None:
        print(f"To jest restauracja {self.name.title()} o typie {self.type}.")

    def show_number_served_clients(self):
        print(f"Obsłużono do tej pory {self.__number_served} klientów")


class IceCreamStand(Restaurant):
    def __init__(self, name: str, type: str, flavors: int) -> None:
        super().__init__(name, type)
        self.__flavors = flavors
    
    def show_flavors(self):
        print(f"Dostępna ilość smaków: {self.__flavors}")

    @property
    def flavors(self):
        return self.__flavors
    
    def add_flavors(self):
        self.__flavors += 1

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

