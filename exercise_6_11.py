cities={'minsk': {'country' : 'Belarus', 'population': 1900000, 'fact' : 'city have metro'}
                , 'gomel': {'country': 'Belarus', 'population' : 900000, 'fact' : 'city have river dnepr'}
                , 'vitebsk': {'country' : 'Belarus', 'population' : 800000, 'fact': 'city have Slavynski bazar'}}
for key,value in cities.items():
    print(key + ':')
    for value in value.values():
        print('\t' , value)