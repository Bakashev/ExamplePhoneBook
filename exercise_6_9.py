favorite_places = {'cuba': ['viktor','sergey','stas'],
                   'dominikana' : ['sergey','yuliya','stepa'],
                   'mexico':['sergey', 'vlad']}

for name,place in favorite_places.items():
    print(name.title() + ' is favorite place: ')
    for i in place:
        print(i.title())