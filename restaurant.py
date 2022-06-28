class Restaurant ():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type


    def describe_restaurant (self):
        print("Restuarant name " + self.name)
        print("Restuarant type is " + self.type)

    def open_restuarant (self):
        print ('Restaurant is open')