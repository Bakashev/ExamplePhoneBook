import json
name = input('Enter you name: ')
fielname = 'user_info.json'
numbers=[3,4,5,6,]
with open(fielname,'w') as f_obj:
    json.dump(name,f_obj)