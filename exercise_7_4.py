# Вводятся дополнения к пицце и выводится сообщение
additions = []
enterAdditins = 'Enter you addition for pizza'
enterAdditins+= '\nIf you need finished enter "q" \n'
while True:
    order = input(enterAdditins)
    if order == 'q':
        break
    else:
        additions.append(order)
        print(order + ' add to your order')

print('Your order pizza whith:')
for i in additions:
    print(i)