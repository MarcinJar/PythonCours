from random import randint
from typing import List
from abc import ABC, abstractmethod
from typing import Protocol

class TicketABC(ABC):
    @abstractmethod
    def values(self) -> List[int | str]:
        pass


class TicketP(Protocol):
    def values(self) -> List[int | str]:
        pass


class Ticket: 
    def __init__(self, values: List[int | str]) -> None:
        self.__values: List[int | str] = values

    def compare(self, ticket: TicketP) -> bool:
        return sorted(map(str, self.__values)) == sorted(map(str, ticket.values))
    
    def show(self):
        print(f"{self.__values}")

    @property
    def values(self) -> List[int | str]:
        return self.__values


class Lottery: 
    def __init__(self) -> None:
        self.__lottery_numbers: tuple[int | str] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F')
        self.__win_ticket: Ticket = None

    def start(self) -> None:
        print("Start new lottery !")
        self.__win_ticket = self.__create_random_ticket()
        print(f"Win ticket:")
        self.__win_ticket.show()
        print("\n")

    def __create_random_ticket(self) -> Ticket:
        lenght = len(self.__lottery_numbers)
        current_runs = []
        for _ in range(4):
            selected_number = randint(0, lenght - 1)
            selected_value = self.__lottery_numbers[selected_number]
            current_runs.append(selected_value)
        return Ticket(current_runs)

    def check_win_ticket(self, ticket: Ticket) -> bool:
        if self.__win_ticket.compare(ticket):
            print(f"You are win! Your ticket is {ticket.values}")
            return True
        
        print("Try again")
        return False

    def get_ticket(self) -> Ticket:
        return self.__create_random_ticket()


