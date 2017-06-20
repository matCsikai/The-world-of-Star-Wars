import requests


def get_planet_data():
    response = requests.get('http://swapi.co/api/planets/').json()
    return response['results']


def formatting_planet_population_data():
    data_of_planets = get_planet_data()
    for planet_data in data_of_planets:
        for key in planet_data:
            if key == 'population' and planet_data['population'] != 'unknown':
                population = int(planet_data['population']) / 1000000
                if population > 1:
                    population = round(population)
                planet_data['population'] = str(population) + ' million people'
    return data_of_planets


def formatting_planet_residents_data():
    data_of_planets = formatting_planet_population_data()
    for planet_data in data_of_planets:
        for key in planet_data:
            if key == 'residents':
                residents = len(planet_data['residents'])
                if residents == 0:
                    planet_data['residents'] = 'No known residents'
                else:
                    planet_data['residents'] = str(residents) + ' known resident(s)'
    return data_of_planets


def formatting_planet_water_data():
    data_of_planets = formatting_planet_residents_data()
    for planet_data in data_of_planets:
        for key in planet_data:
            if key == 'surface_water' and planet_data['surface_water'] != 'unknown':
                surface_water = planet_data['surface_water']
                planet_data['surface_water'] = surface_water + ' %'
    return data_of_planets

def get_required_planet_data():
    data_of_planets = formatting_planet_water_data()
    required_data_of_planets = []
    for planet_data in data_of_planets:
        planet_data_keys = ['name', 'diameter', 'climate', 'terrain', 'surface_water', 'population', 'residents']
        required_planet_data = []
        for key in planet_data_keys:
            if key in planet_data:
                required_planet_data.append(planet_data[key])
        required_data_of_planets.append(required_planet_data)
    return required_data_of_planets



#print(get_required_planet_data())
