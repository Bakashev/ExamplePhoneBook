class Batterry():
    def __init__(self, bettery_size):
        self.battery_size=bettery_size

    def print_betery_size(self):
        print ('Your car can battery for: {}'.format(self.battery_size))

    def get_range (self):
        if self.battery_size == 70:
            self.range=240
        elif self.battery_size >70:
            self.range = 270
        message = 'This car can run {} milies on full carge'.format(self.range)
        print(message)
