users = {
    'aeinstein' : {
        'first' : 'albert',
        'last': 'einstein',
        'location' : 'priceton'
    },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris'
    }
}

for username, user_info in users.items():
    print('\n Username ' + username)
    full_name=user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print('Full name ' + full_name)
    print('Location ' + location)