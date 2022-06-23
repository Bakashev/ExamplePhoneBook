unconfirmed_users=['sergey','vadim', 'igor','sergey']
confirmed_users=[]
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    if current_users in confirmed_users:
        print('Name not use')
    else:
        confirmed_users.append(current_users)
        print('User add ' + current_users.title())

for confirmed_user in confirmed_users:
    print(confirmed_user.title())