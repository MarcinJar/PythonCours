from car import Car

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