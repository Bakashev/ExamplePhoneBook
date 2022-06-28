class Dog():
    """Model dog easy"""
    def __init__(self, name , age):
        """initialization attribute dog"""
        self.name=name
        self.age=age


    def sit(self):
        """Dog sit with command """
        print(self.name.title() + ' sit down')


    def roll_over(self):
        """Dog roll_over"""
        print(self.name + ' roll over')

