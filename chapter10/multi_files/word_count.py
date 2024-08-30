import os
from pathlib import Path

os.system("clear")

def count_word(path: str):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #print(f"Przepraszamy, ale plik {path} nie istnieje.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"Plik {path} zawiera {num_words} słów.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
path_to_directory = 'chapter10/multi_files/files/'

for filename in filenames:
    path = Path(path_to_directory + filename)
    count_word(path)


