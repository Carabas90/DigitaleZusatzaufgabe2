import math

class Pois:
    def __init__(self, rate):
        self.rate = rate

    def pdf(self, x):
        if x >= 0:
           return (((self.rate**x)/(math.factorial(x)))*math.e**(-1*self.rate))
        else:
            return 0

    def cdf(self, x):
        if x > 0:
            res = 0
            for i in range(x+1):
                res += self.pdf(i)
            return res
        else:
            return 0
    
    def erwartungswert(self):
        return self.rate

    def varianz(self):
        return self.rate

    def standardabweichung(self):
        return (math.sqrt(self.varianz()))

if __name__ == "__main__":
    poisson = Pois(3.4)
    print("P(X = 0):", poisson.pdf(0))
    print("P(X <= 2):", poisson.cdf(2))
    print("Erwartungswert:", poisson.erwartungswert())
    print("Varianz:", poisson.varianz())
    print("Standardabweichung:", poisson.standardabweichung())