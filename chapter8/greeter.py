import os
import formatted_name as fn

os.system("clear")

def greet_user(username: str):
    """Wyświetla proste powitanie"""

    username = str(username)

    if not isinstance(username, str):
        raise TypeError("username must be a string")
        
    print(f"Witaj, {username.title()}!")

greet_user("marcin")
greet_user("jan")
greet_user("anna")
greet_user([55, 6])

while True:
    print("\nProszę podać imię i nazwisko:")
    print("(wpisz 'q', azy zakończyć pracę w dowolnym momencie)")
    
    f_name = input("Imię: ")
    if f_name == 'q':
        break

    l_name = input("Nazwisko: ")
    if l_name == 'q':
        break

    formatted_name = fn.get_formatted_name(f_name, l_name)
    print(f"\nWitaj, {formatted_name}!")