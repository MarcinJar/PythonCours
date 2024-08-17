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

    def fill_gas_tank(self):
        print("Zatankowano paliwo !")


class Battery:
    def __init__(self, battery_size:int=40) -> None:
        self.__battery_size = battery_size

    def describe_batery(self):
        print(f"Ten samochód ma akumulator o pojemności {self.__battery_size} kWh")

    def get_range(self):
        if self.__battery_size == 40:
            range = 150
        elif self.__battery_size == 65:
            range = 225
        print(f"Zasięg tego samochodu wynosi około {range} km po poełnym naładwoaniu akumulatora")

    def upgrade_battery(self):
        if self.__battery_size != 65:
            print("Upgrade battery")
            self.__battery_size = 65
        else:
            print("Baterry was upgraded")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("Brak możliwości tankowani - zasilanie elektryczne!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.describe())
my_leaf.fill_gas_tank()
my_leaf.battery.describe_batery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
