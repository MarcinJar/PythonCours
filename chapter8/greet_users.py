import os
from typing import List

os.system("clear")

def greet_users(names: List[str]) -> None:
    for name in names:
        msg = f"Witaj, {name.title()}!"
        print(msg)

usernames = ['halina', 'tymek', 'marzena', 'marcin']
greet_users(usernames)