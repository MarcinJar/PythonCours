import os

from lottery import Lottery

os.system("clear")

lottery = Lottery()

ticket1 = lottery.get_ticket()
ticket2 = lottery.get_ticket()
ticket3 = lottery.get_ticket()

lottery.start()

print(f"Player1 ticket:")
ticket1.show()
lottery.check_win_ticket(ticket1)
print('\n')


print(f"Player2 ticket:")
ticket2.show()
lottery.check_win_ticket(ticket2)
print('\n')


print(f"Player3 ticket:")
ticket3.show()
lottery.check_win_ticket(ticket3)
print('\n')

print("If ypu want to play till win type 'yes'")
try_till_win = input()

if try_till_win == 'yes':
    print("Try till win")
    try_agine = True
    try_number = 0
    while try_agine:
        lottery.start()
        try_agine = lottery.check_win_ticket(ticket1) == False
        try_number += 1

    print(try_number)
    ticket1.show()





