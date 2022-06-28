import dog, car

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