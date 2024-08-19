import os
from pathlib import Path

os.system("clear")

path = Path('chapter10/reading_from_a_file/files/pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

birthday = input("Podaj datę urodzenia (w formacie ddmmrr): ")

if birthday in pi_string:
    print("Twoja data urodzenia znjaduje się wsród miliona pierwszych cyfr liczby pi.")
else:
    print("Nie ma Twoje daty urodzienia wśród pierwszego miliona cyfr liczby pi.")


