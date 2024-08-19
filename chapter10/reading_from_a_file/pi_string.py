import os
from pathlib import Path

os.system("clear")

path = Path('chapter10/reading_from_a_file/files/pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))