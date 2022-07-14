def get_full_city_name(city, country, population = 0):
    if population == 0:
        full_name = city + ', ' +country
    else:
        full_name= city + ', ' +country+ ' - ' + str(population)
    return full_name.title()

