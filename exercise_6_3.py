glos={
    'int' : 'целочисленный формат',
    'tuple' : 'кортеж, не изменяемый объект',
    'list'  : 'список, изменяемый объект, обращение по индексу',
    'dictinory' : 'словарь изменяемый объект, хранит данные ключ:значение'
}

for key, value in glos.items():
    print('\t' + key + ':'+'\n\t\t' + value)
import collections
Test = collections.namedtuple('Test', 'first second name')
test=(Test(1,2,'Igor'))
print(test.name)


favorite_language={
    'Sergey' : 'python',
    'Pavel' : 'java',
    'Stas' : 'C#',
    'Viktor' : 'java'
}

friends=['Pavel', 'Sergey']
for key in sorted(favorite_language.keys()):
    print(key)
    if key in friends:
        print('Hi ' + key + ' your favorite language: ' + favorite_language[key])

print ('\nUse language:')
for value in set(favorite_language.values()):
    print(value)


