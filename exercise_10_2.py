message = 'I like dog very much , dog my favorite animal'
print(message)
message=message.replace('dog', 'cat')
print(message)
print()
file_name='lerning_python.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.replace('Python', 'Java').rstrip())