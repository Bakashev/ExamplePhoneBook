alien_0={'color':'green','point' : 5, 'speed' : 'slow'}
alien_1={'color':'yellow','point' : 10, 'speed' : 'midule'}
alien_2={'color':'red','point':15, 'speed' : 'fast'}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    for key, value in alien.items():
        print(key + ' and ' + str(value))

for i in range(30):
    new_alien = {'color':'green','point' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')
print('Amount aliens ', len(aliens))

for alien in aliens[1:15]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'midule'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15
for alien in aliens:
    print(alien)