visitSity = {}
check = True
while check:
    name = input('Enter your name: ')
    sity = input('What city you have visit: ')
    visitSity[name]=sity
    choose = input(' If you want exit please enter "n" else "y" ')
    if choose == 'n': check = False
for key, value in visitSity.items():
    print('{} want visit {}'.format(key,value))