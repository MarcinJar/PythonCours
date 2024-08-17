import os

os.system("clear")

pets = ['pies', 'kot', 'pies', 'złota rybka', 'kot', 'królik', 'kot']

print("Start with below pets:\n")
print(pets)

while 'kot' in pets:
    pets.remove('kot')

print("\nEnd with below pets:\n")
print(pets)