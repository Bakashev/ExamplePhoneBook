import  restaurant
class IceCreameStand (restaurant.Restaurant):
    def __init__(self,restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = list(flavors)

    def  get_flavours(self):
        print('You choose icecreame with: ')
        for i in self.flavors:
            print (i)

