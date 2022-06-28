import dog, car, electric_car

my_dog=dog.Dog('carry',3)
my_dog.sit()
my_dog.roll_over()
print('My dog name is {}'.format(my_dog.name.title()))
print('My dog age {}'.format(my_dog.age))
your_dog =dog.Dog ('yara',15)
print("Your dog name is {} his {} years old".format(your_dog.name,your_dog.age))


my_car=car.Car('audi','a4',2001)
print(my_car.get_describe_name())
print(my_car.read_odometr())
my_car.odometr_reading=23
print(my_car.read_odometr())
my_car.new_value_odometr(24)
print(my_car.read_odometr())
my_car.post_odometr(45)
print(my_car.read_odometr())

# create electric car descendant
my_electic_car = electric_car.Electic('tesla', ' model s', 2010, 83)
print(my_electic_car.get_describe_name())
print(my_electic_car.odometr_reading)
my_electic_car.describe_bettery()
my_electic_car.fill_gas_tank()
my_car.fill_gas_tank()
my_electic_car.battery_sizy.print_betery_size()

my_electic_car.battery_sizy.print_betery_size()
my_electic_car.battery_sizy.get_range()
