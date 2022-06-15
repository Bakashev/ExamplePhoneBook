age=int(input("Enter age: "))
if age < 4:
    print("free")
elif 4 <=age < 18:
    print('Bilet cost 5$')
else:
    print('Bilet cost 10$')

age=int(input('Enter age'))
if age <4:
    cost=0
elif 4<=age<18:
    cost=5
else:
    cost=10
print('Bilet coast {} $'. format(cost))
