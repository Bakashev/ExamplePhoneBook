class Car ():
    """Car model easy"""
    def __init__(self, make, model, year ):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_describe_name (self):
        """Return car describe"""
        long_name = 'You car {}  {} in {}'.format(self.make,self.model,self.year)
        return long_name
    def read_odometr(self):
        info = 'This car has {} milies on it'.format(self.odometr_reading)
        return info

    def post_odometr(self,value):
        if value < 0:
            print('You can not enter this value')
        else:
            self.odometr_reading+=value


    def new_value_odometr (self,milies):
        if milies<self.odometr_reading:
            print('This operation is fail')
        else:
            self.odometr_reading=milies