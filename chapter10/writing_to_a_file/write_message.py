import os
from pathlib import Path

os.system("clear")

contents = "Uwielbiam programować.\n"
contents += "Uwielbiam tworzyć gry.\n"
contents += "Uwielbiam pracować z danymi.\n"

path = Path('chapter10/writing_to_a_file/files/programming.txt')

path.write_text(contents)