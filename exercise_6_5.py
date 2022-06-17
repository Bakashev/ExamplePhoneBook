rivers={
    'nile':'egypt',
    'dnepr' : 'ukrain',
    'volga' : 'russia',
    'berezino' : 'belarus'
}

for key, values in rivers.items():
    print('The ' + key.title() + ' runs through ' + values.upper())
print()
for key in rivers.keys():
    print(key.title())

print()
for value in rivers.values():
    print(value.title())