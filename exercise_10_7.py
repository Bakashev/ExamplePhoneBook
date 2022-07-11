numberOne = input('Press number one: ')
numberTwo = input('Press number two: ')
while format(numberOne) != int  and format(numberTwo)!= int:
    try:
        numberOne = int(numberOne)
        numberTwo = int(numberTwo)
    except ValueError:
        if format(numberOne) != int:
            print('You enter not number one: {} '.format(numberOne))
            numberOne = input('Press number one: ')

        if format(numberTwo) != int:
            print('You enter not number two :{} '.format(numberTwo))
            numberTwo = input('Press number two: ')
    else:
        rezult = numberOne+numberTwo
        print(rezult)
        break