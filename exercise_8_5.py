def describe_city(city_name,city_country = 'Belarus'):
    """Print city and country"""
    print(city_name.title() + ' is in '+ city_country.title())
describe_city('minsk')
describe_city('kiev', 'ukrain')