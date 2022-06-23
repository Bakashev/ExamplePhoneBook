promt = 'Enter city which you have visited '
promt += '\n Enter quit when you enter finished'
while True:
    city = input(promt)

    if city == 'quit':
        break
    else: print (city)