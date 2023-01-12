class Country:
    def __init__(self, population=0):
        self._population = population
   
    def getPopulation(self):
        return self._population

    def setPopulation(self, population):
        self._population = population


class Russia(Country):
    pass


class Canada(Country):
    pass


class Germany(Country):
    pass


Moskow = Russia()
Ottava = Canada()
Berlin = Germany()

Moskow.setPopulation(10500000)
Ottava.setPopulation(320000000)
Berlin.setPopulation(15000000)


print(Moskow.getPopulation())
print(Ottava.getPopulation())
print(Berlin.getPopulation())
