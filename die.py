import  random
class Die():
    def __init__(self, sides =6):
        self.sides=sides

    def roll_die(self, amount = 6):
        for i in range(amount):
            print(random.randint(1,self.sides))

