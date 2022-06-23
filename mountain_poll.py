polling_active = True
nameDict={}
while polling_active:
    name = input('Enter your name')
    response = input('How old are you')
    nameDict[name] = response
    quit = input('Would you like answer y/n')
    if quit == 'n':
        polling_active = False
print(nameDict)