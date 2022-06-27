def city_country (city,country):
    info = city + ' ' + country
    return info.title()

info = city_country( country='belarus', city= 'minsk')
print(info)
print(city_country('vancuver', 'canada'))