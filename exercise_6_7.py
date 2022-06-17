personOne={'first_name':'Yulia',
        'last_name' : 'Bakasheva',
        'age' : 35,
        'city':'Minsk'
        }
personTwo={'first_name':'Sergey',
        'last_name' : 'Bakashev',
        'age' : 36,
        'city':'Minsk'
        }
personThree={'first_name':'Alina',
        'last_name' : 'Bakasheva',
        'age' : 6,
        'city':'Minsk'
        }
personFour={'first_name':'Yulia',
        'last_name' : 'Bakasheva',
        'age' : 35,
        'city':'Minsk'
        }
peoples =[personOne,personTwo,personThree,personFour]
for people in peoples:
    print('Person info: ')
    for info in people.items():
        print('\t', info[1] )