import json
numbers= [3,6,45,2,1,3,98,-1]
fielname='numbers.json'
with open(fielname, 'w') as f_obj:
    json.dump(numbers,f_obj)


