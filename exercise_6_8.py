Kery ={'type' : 'dog ', 'owner' : 'Tanya'}
Baby = {'type' :  'turtel', 'owner' : 'Lelik'}
Persik = {'type' : 'cat', 'owner' : 'Ira'}

pets=[Kery,Baby,Persik]
for pet in pets:
    print('Info :')
    for key, val in pet.items():
        print('\t', key, val)

