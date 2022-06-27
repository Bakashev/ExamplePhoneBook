def make_cars(made, model, **args):
    cars_info={}
    cars_info['made_in'] = made
    cars_info['model'] = model
    for key, value in args.items():
        cars_info[key]=value
    return cars_info

car = make_cars('China', 'Haval', v=1.6, speed_max=200, color = 'black' )
print(car)
