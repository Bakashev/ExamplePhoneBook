favorite_language={
    'Sergey' : 'python',
    'Pavel' : 'java',
    'Stas' : 'C#',
    'Viktor' : 'java'
}

peoples=['Sergey','Pavel','Yuliya','Alina','Darya']
for people in peoples:
    if people in favorite_language.keys():
        print('Thank you {} for participation '. format(people))
    else:
        print(format(people) + ' Do you participation? ')