import os

os.system("clear")

def describe_pet(pet_name: str, animal_type: str="pies"):
    print(f"\nMoje zwierzę to {animal_type}")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}")

describe_pet(pet_name="harry", animal_type="chomik")
describe_pet("puszek", "kot")
describe_pet("azor")
describe_pet(pet_name="łatek")