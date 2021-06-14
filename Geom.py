import math

class Geom:
    def __init__(self, p):
        self.p = p
        self.q = 1-p

    def pdf(self, x):
        if x > 0:
           return (self.p * self.q**(x-1))
        else:
            return 0

    def cdf(self, x):
        if x > 0:
            return (1-self.q**x)
        else:
            return 0
    
    def erwartungswert(self):
        return (1/self.p)

    def varianz(self):
        return (self.q/self.p**2)

    def standardabweichung(self):
        return (math.sqrt(self.varianz()))

if __name__ == "__main__":
    geometrisch = Geom(0.4)
    print("P(X = 2):", geometrisch.pdf(2))
    print("P(X <= 4):", geometrisch.cdf(4))
    print("Erwartungswert:", geometrisch.erwartungswert())
    print("Varianz:", geometrisch.varianz())
    print("Standardabweichung:", geometrisch.standardabweichung())