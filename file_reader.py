with open('pi_digits.txt') as file_object:
    contents= file_object.read()
    print(contents.rstrip())
pi_digits=open('d:\Work\ExamplePhoneBook\pi_digits.txt', 'r')
print(pi_digits.read())
pi_digits.close()

file_name='pi_digits.txt'
with open(file_name) as file_object:
    list_file=[]
    for str in file_object:
        print(str.rstrip())
        list_file.append(str.strip())
print(list_file)


file_name='pi_digits.txt'
with open(file_name) as file_object:
    pi_string = ''
    for line in file_object:
        pi_string+=line.strip()
    print(pi_string)

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string += line.strip()
print(line.strip())
birthday=input('enter birthday')
