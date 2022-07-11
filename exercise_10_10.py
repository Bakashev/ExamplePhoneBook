fielname = 'magic.txt'
with open(fielname) as f_obj:
    content = f_obj.read()
    print(content.count('name'))