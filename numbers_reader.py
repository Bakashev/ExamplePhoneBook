import json
fielname = 'numbers.json'
with open(fielname) as f_obj:
    numbers = json.load(f_obj)
print(numbers)