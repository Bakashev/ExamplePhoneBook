pets=['dog' , 'cat' , 'mouse', 'cat', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

def describe_pet(animal_type, animal_name):
    """View information fo animal"""
    print('I have ' + animal_type)
    print('Here name is {} '.format(animal_name))
describe_pet('dog','Karry')
#describe_pet()