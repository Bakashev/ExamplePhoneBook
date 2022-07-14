from name_funcation import get_formated_name
print('Enter q to quit')
while True:
    first = input("Enter first name: ")
    if first == 'q':
        break
    last = input('Enter last name: ')
    if first == 'q':
        break
    second=input('Enter second name: ')
    if second=='q':
        break
    formated_name= get_formated_name(first,last,second_name=second)
    print('Your full name is {}'.format(formated_name))