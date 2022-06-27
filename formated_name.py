def fullName(firstName,secondName):
    full_name=firstName + ' ' + secondName
    return full_name.title()
print('Hellow {}'.format(fullName('bakashev', 'sergey')))

def fullNameOne (firstName,last_name,middle_name=''):
    if middle_name:
        full_name = firstName + ' ' + last_name + ' ' + middle_name
    else:
        full_name = firstName + ' ' + last_name
    return full_name.title()
info=fullNameOne('bakashev','sergey')
print(info)
info=fullNameOne('bakashev','sergey','olegovich')
print(info)