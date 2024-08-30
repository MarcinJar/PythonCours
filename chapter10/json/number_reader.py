import os
from pathlib import Path
import json
from typing import List

os.system("clear")

path = Path('chapter10/json/files/numbers.json')

contents = path.read_text()
print(contents[0:3])

numbers: List[int] = json.loads(contents)
print(numbers[0:3])