import os

os.system("clear")

class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.__make = make
        self.model = model
        self.year = year
        self.__odometer = 0

    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, value):
        self.__make = value

    @property
    def odometer(self):
        return self.__odometer      

    @odometer.setter
    def odometer(self, value):
        if value >= self.__odometer:
            self.__odometer = value
        else:
            print(f"Nie można cofnąć licznika przebiegu samochodu!")

    def increment_odometer(self, value):
        if value >= 0:
            self.__odometer += value
        else:
            print(f"Nie można cofnąć licznika przebiegu samochodu!")


    def describe(self) -> str:
        longName = f"{self.year} {self.__make} {self.model}"
        return longName.title()
    
    def read_odometer(self):
        print(f"Ten samochód ma przejechane {self.__odometer} km")



my_new_car = Car('audi', 'a4', 2024)

print(my_new_car.describe())
my_new_car.read_odometer()

print(my_new_car.make)
my_new_car.make = "BMW"
print(my_new_car.make)

my_new_car.odometer = 147
my_new_car.read_odometer()

my_new_car.odometer = 100_000

my_new_car.odometer = 230
my_new_car.read_odometer()

my_new_car.increment_odometer(300)
my_new_car.read_odometer()
