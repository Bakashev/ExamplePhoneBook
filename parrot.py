promt='\nTell me something and I will repeat it back to you'
promt+='\n Enter quit to and the program '

active = True
while active:
    message=input(promt)
    if message=='quit':
        active=False
    else:print(message)

