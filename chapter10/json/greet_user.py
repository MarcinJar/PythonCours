import os
from pathlib import Path
import json

os.system("clear")

path = Path('chapter10/json/files/username.json')

contents = path.read_text()
username = json.loads(contents)

print(f"Witamy ponownie, {username}")