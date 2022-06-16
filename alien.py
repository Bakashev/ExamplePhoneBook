alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
alien_1={}
alien_1['point']=1
alien_1['name']='Andrey'
print(alien_1)
alien_2={}
alien_2['color']= 'green'
print('Alien color ' + alien_2['color'])
alien_2['color'] = 'red'
print('Alien color now ' + alien_2['color'])
alien_3={'x_position':0,'y_position':25,'speed' : 'medium'}
print('Original position ' + str(alien_3['x_position']))
if alien_3['speed']=='slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_3['x_position']  += x_increment

print("Next x position " + str(alien_3['x_position']))

del alien_0['points']
print(alien_0)

favorite_languages={
    'Sergey' : 'python',
    'Pavel' : 'java',
    'Stas' : 'C#',
    'Viktor' : 'java',
    'Dmitri' : 'viper'
    }
print(favorite_languages)
print('Viktor favorite languges ' + favorite_languages['Viktor'].title())