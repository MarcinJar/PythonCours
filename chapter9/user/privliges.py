from typing import List

class Privliges: 
    def __init__(self, privliges: List[str]) -> None:
        self.__privliges = privliges

    def show_privliges(self):
        print("Dostępne uprawnienia: ")
        for privlige in self.__privliges:
            print(f"\t{privlige.upper()}")