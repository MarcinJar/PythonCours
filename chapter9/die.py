from random import randint

class Die:
    def __init__(self, sides: int=6) -> None:
        self.__sides = sides

    def roll_die(self) -> int:
        return randint(1, self.__sides)
    
    @property
    def sides(self) -> int:
        return self.__sides
    

class GameDie:
    def __init__(self) -> None:
        self.__die: Die = None
        self.__runs: int = 0

    def play(self):
        if self.__die == None or self.__runs == 0:
            print(f"Can not start game, die: {self.__die} and runs: {self.__runs}")
            return
        
        print(f"Die with {self.__die.sides} sides and {self.__runs} runs")
        for run in range(self.__runs):
            print(f"run {run}: {self.__die.roll_die()}")

    def set_die(self, die: Die):
        self.__die = die 

    def set_runs_number(self, runs: int):
        self.__runs = runs