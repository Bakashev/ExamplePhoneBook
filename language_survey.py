import survey
question = survey.AnonymousSurvey('What is your name?')
question.show_question()
while True:
    answer = input('Name: ')
    if answer == 'q':
        break
    question.store_response(answer)
question.sho_rezult()

