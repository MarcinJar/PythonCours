import os
from pathlib import Path

os.system("clear")

path = Path('chapter10/writing_to_a_file/files/guest.txt')

names = ""

print("Type q to finish")

while True:
    name = input("Pleas type your name: ")
    if name == "q":
        break
    names += f"{name}\n"
    path.write_text(names)
    