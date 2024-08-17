from typing import List

from .user import User
from .privliges import Privliges

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, privliges: List[str]) -> None:
        super().__init__(first_name, last_name, age)
        self.privliges = Privliges(privliges)