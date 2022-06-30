file_name='lerning_python.txt'
with open(file_name) as file_object:
    print(file_object.read())

print()
with open('lerning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

print()
with open('lerning_python.txt') as file_object:
    lines=file_object.readlines()
for line in lines: print(line.rstrip())
