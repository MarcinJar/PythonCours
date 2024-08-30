import os
from pathlib import Path
import json

os.system("clear")

path = Path('chapter10/json/files/numbers.json')

numbers = [2, 3, 5, 7, 11, 13]

contents = json.dumps(numbers)
path.write_text(contents)