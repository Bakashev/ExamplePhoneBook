def greeter_user(*name):
    for i in name:
        print('Hellow {}'. format(i.title()))

greeter_user('sergey', 'yuliya', 'alina', 'dasha')