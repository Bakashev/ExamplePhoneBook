car=input('What car are you want rent? ')
print('Let me see if I can find you a {}'.format(car))

seat=int(input('Wht amount seat you need?'))
if seat>8:
    print('You need wait')
else:
    print("Your table ready")

number=int(input('Enter number: '))
if number%10==0:
    print("You enter correct number")
else: print('Try again')


