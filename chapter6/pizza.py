import os

os.system('clear')

pizza = {
    'crust': 'grubym',
    'toppings': ['pieczarki', 'podwójny ser']
}

print(f"Zamówiłeś pizzę na {pizza['crust']} cieście z następującymi dodatkami")
for topping in pizza["toppings"]:
    print(f"\t{topping}")