favorite_numbers={'sergey':(3,5,6), 'stepa': (1,88,9)
                  ,'yuliya':(55,7,2)}
for key,value in favorite_numbers.items():
    print(key.title() + " favorite numbers is : ")
    for i in value:
        print(i)