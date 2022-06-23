sandwich_orders=['postrami','meat' ,'postrami', 'vegetable', 'frut', 'postrami']
finished_sandwich=[]
for sanwich in sandwich_orders:
    print("I made your {} sandwich ". format(sanwich))
print('Postrami not found')
while 'postrami' in sandwich_orders:
    sandwich_orders.remove('postrami')
while sandwich_orders:
    currentItems = sandwich_orders.pop()
    finished_sandwich.append(currentItems)
    print('Sandwich {} ready'.format(currentItems))
print(finished_sandwich)
