class City:
    all_cities = []

    def __init__(self, name, population, country):
        self.name = name
        self.population = population
        self.country = country
        self.add_city(name)

    def add_city(self, city_name):
        self.all_cities.append(city_name)


if __name__ == '__main__':
    malaga = City('Malaga', 569005, 'Spain')
    boston = City('Boston', 689326, 'USA')
    beijing = City('Beijing', 21540000, 'China')

    print(malaga.all_cities)  # This should print "['Malaga', 'Boston', 'Beijing']".
