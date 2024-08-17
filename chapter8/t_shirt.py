import os

os.system("clear")

def make_shirt(text: str="uwielbiam pythona!", size: int=130):
    print(f"\nKoszulka o rozmiarze: {size}")
    print(f"Z nadrukiem: {text.title()}")

make_shirt("Ucze się pythona!", 100)
make_shirt(size=65, text="Lubię czytać")
make_shirt()
make_shirt(size=80)

