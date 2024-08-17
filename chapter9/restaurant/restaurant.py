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