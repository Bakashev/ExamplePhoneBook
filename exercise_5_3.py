alien_color = 'green'
if alien_color == 'green':
    print('You got 5 points')
alien_color=input('Enter color')
if alien_color == 'green':
    print('You got 5 points')
elif alien_color == 'yelow':
    print('You got 10 points')
elif alien_color=='red':
    print('You got 15 points')

age=int(input('Enter your age: '))
if age<2:
    name='baby'
elif 2<=age<4:
    name = 'small'
elif 4<=age<13:
    name='child'
elif 13<=age<20:
    name='tinedger'
elif 20<=age<65:
    name = 'adult'
elif age>65:
    name = 'elder'
print('Your age {} '.format(name))


fruit = input('Enter fruit:')
favorite_fruits= ['apple','orange','banana','kivi']
if fruit in favorite_fruits:
    print('You really like {} !'.format(fruit))


