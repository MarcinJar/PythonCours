import os

os.system("clear")

prompt = "Jeżeli powiesz nam, kim jesteś, spersonalizujemy wyświetlany komunikat."
prompt += "\nJam masz na imię? "

name = input(prompt)
print(f"Witaj, {name}")
