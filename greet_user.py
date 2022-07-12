import json
def get_stored_username():
    """Get user name if it true"""
    fielname = 'user_info.json'
    try:
        with open(fielname) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user ():
    """Use save user if file not found we will create new file and write user name"""
    fielname = 'user_info.json'
    username= get_stored_username()
    if username:
        print('Well come back {}'.format(username))
    else:
        with open(fielname,'w') as f_obj:

            name = input('Enter you name: ')
            json.dump(name,f_obj)

