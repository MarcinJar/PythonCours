import os
from typing import List

os.system("clear")

class User:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__login_attempts = 0

    def describe(self) -> None:
        print(f"To jest urzytkownik {self.first_name.title()} {self.last_name.title()} o wieku {self.age}.")

    def greet(self) -> None:
        print(f"Witaj, {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self):
        self.__login_attempts += 1

    @property
    def login_attempts(self):
        return self.__login_attempts
    
    def show_number_login_attepmpts(self):
        print(f"Prób logowania odnotowano: {self.login_attempts}")

    def reset_login_attepmpts(self):
        print("Reset login attepmts")
        self.__login_attempts = 0


class Privliges: 
    def __init__(self, privliges: List[str]) -> None:
        self.__privliges = privliges

    def show_privliges(self):
        print("Dostępne uprawnienia: ")
        for privlige in self.__privliges:
            print(f"\t{privlige.upper()}")


class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, privliges: List[str]) -> None:
        super().__init__(first_name, last_name, age)
        self.privliges = Privliges(privliges)


marcin = User(first_name='marcin', last_name='Jarmułowski', age=32)
anna = User(first_name='anna', last_name='kowlaska', age=39)
jan = User(first_name='jan', last_name='nowak', age=57)

marcin.increment_login_attempts()
marcin.describe()
marcin.increment_login_attempts()
marcin.greet()
marcin.increment_login_attempts()
marcin.show_number_login_attepmpts()
marcin.reset_login_attepmpts()
marcin.show_number_login_attepmpts()
print("\n")

anna.increment_login_attempts()
anna.describe()
anna.greet()
anna.show_number_login_attepmpts()
anna.reset_login_attepmpts()
anna.show_number_login_attepmpts()
print("\n")

jan.increment_login_attempts()
jan.describe()
jan.greet()
jan.increment_login_attempts()
jan.increment_login_attempts()
jan.increment_login_attempts()
jan.increment_login_attempts()
jan.show_number_login_attepmpts()
jan.reset_login_attepmpts()
jan.show_number_login_attepmpts()
print("\n")

admin = Admin("Tomasz", "Nowak", 45, ["add user", "remove user", "show all users", "read content"])
admin.increment_login_attempts()
admin.describe()
admin.greet()
admin.show_number_login_attepmpts()
admin.privliges.show_privliges()
admin.reset_login_attepmpts()
admin.show_number_login_attepmpts()