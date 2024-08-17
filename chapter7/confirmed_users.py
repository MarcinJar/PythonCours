import os

os.system("clear")

unconfirmed_users = ['alicja', 'bartek', 'katarzyna']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Werfikacja użytkownika: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nZwerfikowano wymienionych poniżej użytkowników: ")
for confirmed_user in sorted(confirmed_users):
    print(confirmed_user.title())