# buy ticket
while True:

    age= int(input('Enter your age:'))
    if age < 3: print("Ticket free")
    elif 3 <= age < 12 : print('ticket cost 10$')
    elif age >= 12: print('Ticket cost 15$')
    break

active=True
while active:
    age = int(input('Enter your age:'))
    if age < 3:
        print("Ticket free")
    elif 3 <= age < 12:
        print('ticket cost 10$')
    elif age >= 12:
        print('Ticket cost 15$')
    active = False

age = ''
while age !='q':
    age = input('Enter you age or enter q to exit')
    if age == 'q':
        break
    age = int(age)
    if age < 3:
        print("Ticket free")
    elif 3 <= age < 12:
        print('ticket cost 10$')
    elif age >= 12:
        print('Ticket cost 15$')
