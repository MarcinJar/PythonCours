import os

os.system("clear")

responses = {}
polling_active = True
while polling_active:
    name = input("\nJak masz na imię: ")
    response = input("\nJakie masz hobby? \n")
    responses[name] = response
    repeat = input("Czy ktokolwiek inny chce wziąć udzial w nakiecie? ()tak/nie")
    if repeat == 'nie':
        polling_active = False

print("\n--- Wyniki ankiety ---")
for name, response in responses.items():
    print(f"{name} hobby jest {response}")

