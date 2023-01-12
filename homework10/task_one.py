class Country:
    def __init__(self, population):
        pass


class Russia(Country):
    def __init__(self, population=0):
        self._population = population
   
    def get_population(self):
        return self._population

    def set_population(self, population):
        self._population = population


class Canada(Country):
    def __init__(self, population=0):
        self._population = population
    
    def get_population(self):
        return self._population
        
    def set_population(self, population):
        self._population = population


class Germany(Country):
    def __init__(self, population=0):
        self._population = population

    def get_population(self):
        return self._population

    def set_population(self, population):
        self._population = population


Moskow = Russia()
Ottava = Canada()
Berlin = Germany()

Moskow.set_population(10500000)
Ottava.set_population(320000000)
Berlin.set_population(15000000)


print(Moskow.get_population())
print(Ottava.get_population())
print(Berlin.get_population())

print(Moskow._population)
print(Ottava._population)
print(Berlin._population)
