import os

os.system("clear")

hight = input("Ile masz wzrostu (w centymetrach)? ")
hight = int(hight)

if hight >= 90:
    print("\nJesteś wystarczająco wysoki na przejażdżkę!")
else:
    print("\nBędziesz mógł się przejechać, gdy nieco uroścniesz.")

