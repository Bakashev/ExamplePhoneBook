import car, battery_info
class Electic (car.Car):
    """Electic car aspect"""
    def __init__(self,make,model,year, bettery_size =70):
        super().__init__(make,model,year)
        self.battery_sizy=battery_info.Batterry(bettery_size)

    def describe_bettery (self):
        """print information with battery"""
        print(" {2} {1} has battery {0} kw".format(self.battery_sizy, self.model, self.make.title()))

    def fill_gas_tank (self):
        print("Electrocar not need gas")
