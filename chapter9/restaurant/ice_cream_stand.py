from .restaurant import Restaurant

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