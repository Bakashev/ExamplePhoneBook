curren_users=['Sergey', 'Andrey', 'Ivan', 'Max', 'Stephan']
new_users=['Alina','SERGEY','Ivan', 'Veronika','Ira']
for new_user in new_users:
    print('You enter name:' + new_user )
    for curren_user in curren_users:
            if new_user.lower()==curren_user.lower():
                print( new_user + ' this name use ' + ' Enter new name')