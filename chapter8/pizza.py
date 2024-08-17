# import os

# os.system("clear")

def make(size: int, *toppings) -> None:
    print(f"\nPrzygotowuję pizzę o wielkości {size} cm, z następującymi dodatkami: ")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza(40, 'peperoni')
# make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')
