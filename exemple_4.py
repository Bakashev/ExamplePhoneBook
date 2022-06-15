#create list magicians
magicians=['alice','david','carolin']
for magician in magicians:
    print(magician.title() + ', that was a great trick ')
    print("I can't wait to see your next trick " + magician.title() + '\n')
print('Thanks for the great show')

#range
for i in range(1,6):
    print(i)

#create list for range
listRang=list(range(1,6))
print(listRang)

listRangTwo=list(range(2,11,2))
print(listRangTwo)

square=[]
for i in range(1,11):
    square.append(i**2)
print(square)

squareTwo=[val**2 for val in range(1,11)]
print(squareTwo)

players=['charles','martina','eli','michel','florence']
print(players[0:2])
print(players[:-1])
print(players[-3:])

for player in players[-3:]:
    print(player.title())

my_food=['pizza','falafel','carrot cake']
friend_food=my_food[:]
print(my_food)
print(friend_food)
my_food.append('tomato')
friend_food.append('potato')
print(my_food,friend_food)