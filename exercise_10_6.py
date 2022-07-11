numberOne = input('Press number one: ')
numberTwo = input('Press number two: ')
try:
    numberOne = int(numberOne)
    numberTwo = int(numberTwo)
except ValueError:
    if format(numberOne) != int:
        print('You enter not number one: {} '.format(numberOne))
    if format(numberTwo) != int:
        print('You enter not number two :{} '.format(numberTwo))
else:
    rezult = numberOne+numberTwo
    print(rezult)