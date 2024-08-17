import os

os.system('clear')

alien_0 = {'color': 'zielony', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print(alien_0)

alien_0['color'] = 'czerwony'

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

del alien_0['points']
print(alien_0)

print(alien_0.get('points', 'Brak przypisanych punktów'))
print(alien_0.get('points'))