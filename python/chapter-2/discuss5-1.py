from math import sqrt

def distance(city1, city2):
    lat_1, lon_1 = get_lat(city_1), get_lon(city_1)
    lat_2, lon_2 = get_lat(city_2), get_lon(city_2)
    return sqrt((lat_1 - lat_2) ** 2 + (lon_1 - lon_2) ** 2)

def closer_city(lat, lon, city1, city2):
    new_city = make_city('arb', lat, lon)
    if distance(new_city, city1) < distance(new_city, city2):
        return get_name(city1)
    return get_name(city2)
