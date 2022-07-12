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

def get_new_username():
    """Create new user name"""
    fielname='user_info.json'
    name = input("Ente your name: ")
    with open(fielname,'w') as f_obj:
        json.dump(name,f_obj)

def greet_user ():
    """Use save user if file not found we will create new file and write user name"""
    fielname = 'user_info.json'
    username= get_stored_username()
    if username:
        print('Well come back {}'.format(username))
    else:
        get_new_username()
