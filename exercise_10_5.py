message=input('Why you love progrmming ?')
while message:
    file_name='answer_question.txt'
    with open(file_name,'a') as file_object:
        file_object.write(message + '\n')
    message = input('Why you love progrmming ?')


