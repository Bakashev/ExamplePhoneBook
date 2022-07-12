import json
fielname = 'user_info.json'
try:
    with open(fielname) as f_obj:
        username = json.load(f_obj)
        print('Well come back {}'.format(username))
except FileNotFoundError:
    with open(fielname,'w') as f_obj:
        name = input('Enter you name: ')
        json.dump(name,f_obj)


