import os
from pathlib import Path

os.system("clear")

path = Path('chapter10/events/files/alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Przepraszamy, ale plik {path} nie istnieje.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"Plik {path} zawiera {num_words} słów.")
