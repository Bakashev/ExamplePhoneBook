check = True
while check:
    name = input('Enter your name or enter "q" for exit: ')
    if name == 'q':
        print('See you later')
        check=False
    else:
        file_name='guest_book.txt'
        with open(file_name,'a') as file_object:
            print("Hello {} we glade to see you ".format(name.title()))
            file_object.write("Hello {} we glade to see you \n  ".format(name.title()))