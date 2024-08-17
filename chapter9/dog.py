import os

os.system("clear")

class Dog:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def sit(self) -> None:
        print(f"{self.name.title()} teraz siedzi.")

    def roll_over(self) -> None:
        print(f"{self.name.title()} teraz położył się na plecy!")


myDog = Dog('willie', 6)

print(f"Mój pies ma na imie {myDog.name.title()}.")
print(f"Mój pies ma {myDog.age} lat.")

myDog.sit()
myDog.roll_over()
