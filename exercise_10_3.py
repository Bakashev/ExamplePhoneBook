name = input("Enter your name: ")
file_name='guest.txt'
with open(file_name,'w') as file_object:
    file_object.write('Hellow dear guest. We are glade to see you {}'.format(name.title()))
