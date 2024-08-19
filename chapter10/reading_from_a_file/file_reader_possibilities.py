import os
from pathlib import Path

os.system("clear")

path = Path('chapter10/reading_from_a_file/files/learning_python.txt')
contents = path.read_text()

print(contents)
print("\n")

for line in contents.splitlines():
    print(line.replace('Pythonie', 'C#'))
