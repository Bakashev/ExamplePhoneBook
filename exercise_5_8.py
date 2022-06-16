names=['Sergey', 'Andrey', 'Ivan', 'Max', 'Stephan', 'admin']
if names:
    for name in names:
        if name == 'admin':
            print('Hellow ' + name + ' would you like to see a status report')
        else:
            print('Hellow ' + name)
else:
    print('We need to find some users')