my_pizza=['margarita','meat','chease']
friend_pizzas=my_pizza[:]
my_pizza.append('neopolitan')
friend_pizzas.append('vegetables')
print('My favorite pizza are:')
for i in my_pizza:
    print(i)
print("\nFavorit pizza my friend 's are: ")
for i in friend_pizzas:
    print(i)