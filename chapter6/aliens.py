import os

os.system('clear')

alien_0 = {'color': 'zielony', 'points': 5}
alien_1 = {'color': 'żółty', 'points': 10}
alien_2 = {'color': 'czerwpny', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\nNowa lista wypełnona wygenerowanymi obcymi:")

aliens_new = []

for alien_number in range(30):
    new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
    aliens_new.append(new_alien)

for alien in aliens_new[:3]:
    if alien['color'] == 'zielony':
        alien['color'] = 'żółty'
        alien['speed'] = 'średnio'
        alien['points'] = 10

for alien in aliens_new[:5]:
    print(alien)

print(f"Całkowita liczba obcych: {len(aliens_new)}")
