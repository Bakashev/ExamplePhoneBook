import json
fielname = 'user_info.json'
with open(fielname) as f_obj:
    username = json.load(f_obj)
    print(username)