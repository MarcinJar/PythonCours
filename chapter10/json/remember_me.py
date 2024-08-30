import os
from pathlib import Path
import json
from typing import Dict

os.system("clear")

def get_stored_user_data(path: Path) -> Dict[str, str] | None:
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    return None

def get_new_user_data(path: Path) -> Dict[str, str]:
    username = input("Jak masz na imię? ")
    age = input("Ile masz lat? ")
    hobby = input("Jakie masz hobby? ")
    data = {"username": username, "age": age, "hobby": hobby}
    contents = json.dumps(data)
    path.write_text(contents)
    return contents

def user_info():
    path = Path('chapter10/json/files/username.json')
    data = get_stored_user_data(path)
    if data:
        print(f"Witamy ponownie, informacje o osobie: {data}")
        new = input("Czy to poprawne dane? (yes/no) ")
        if new == "no":
            data = get_new_user_data(path)
            print(f"Twoje podane dane to: {data}")
    else:
        data = get_new_user_data(path)
        print(f"Twoje podane dane to: {data}")


user_info()
