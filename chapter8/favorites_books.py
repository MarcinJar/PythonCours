import os

os.system("clear")

def favorite_book(book: str):
    book = str(book)
    print(f"Jedną z moich ulubionych książek jest {book.title()}")

favorite_book("Python, poradnik dla programisty")
favorite_book("Hary Potter")
favorite_book(1234)