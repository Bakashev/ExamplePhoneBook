pizza={
    'crust' : 'thick',
    'toppings' : ['mushrooms' , 'extra cheese']
}

print("You ordered a " + pizza['crust'] + " - crust pizza" +
      ' with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)

favorite_language={
    'Sergey' : ['python' , 'SQL'],
    'Pavel' : ['java'],
    'Stas' : ['C#'],
    'Viktor' : ['java']
}

for key, value in favorite_language.items():
    if len(value)<2:
        print(key, 'favorite language :' + '\n', value[0])
    else:
        print(key, 'favorite languages: ')
        for languge in value:
            print('',languge)

def make_pizza(*topping):
    print('Making a pizza with a folowing topping')
    for topping in topping:
        print (' - ' + topping)

make_pizza('pepperoni')
make_pizza('mashrooms', 'green peppers')