
pizzas = ['peperoni', 'hawajska', 'polska', 'góralska', 'owoce morza']

# for pizza in pizzas:
#     print(f"Lubię pizzę {pizza.title()}")

# print("Naprawdę uwielbiam pizzę")

# first_tree_elements = pizzas[:3]
# print("Pierwsze trzy elementy listy to:")
# for pizza in first_tree_elements:
#     print(pizza.title())

# middle_tree_elements = pizzas[1:4]
# print("Trzy elementy w środku listy to:")
# for pizza in middle_tree_elements:
#     print(pizza.title())

# last_tree_elements = pizzas[-3:]
# print("Ostatnie trzy elementy listy to:")
# for pizza in last_tree_elements:
#     print(pizza.title())

friend_pizzas = pizzas[:]
pizzas.append("salami")
friend_pizzas.append("wege")

print("Moje ulubione pizze: ")
for i, p in enumerate(pizzas): 
    print(f"{i+1} - {p.title()}")

print("Mojego przyjaciela ulubione pizze:")
for i, p in enumerate(friend_pizzas): 
    print(f"{i+1} - {p.title()}")