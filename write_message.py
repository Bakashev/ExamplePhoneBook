file_name = 'write_messga.txt'
with open(file_name,'a') as file_object:
    file_object.write('\nHellow world\n')
    file_object.write(('I love progrmming\n\n'))
    file_object.write('Add string')
