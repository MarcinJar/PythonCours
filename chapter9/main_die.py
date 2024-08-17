import os

from die import GameDie, Die

os.system("clear")

die6 = Die()
die10 = Die(10)
die20 = Die(20)

game1 = GameDie()
game1.set_die(die6)
game1.set_runs_number(10)
game1.play()
print("\n")

game2 = GameDie()
game2.set_die(die10)
game2.set_runs_number(10)
game2.play()
print("\n")

game3 = GameDie()
game3.set_die(die20)
game3.set_runs_number(10)
game3.play()
print("\n")