import math

class Bin:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.q = 1-p

    def pdf(self, x):
        if x >= 0:
           return (math.comb(self.n, x) * (self.p**x) * (self.q**(self.n-x)))
        else:
            return 0

    def cdf(self, x):
        if x > 0 and x < self.n:
            res = 0
            for i in range(x+1):
                res += self.pdf(i)
            return res
        elif x > self.n:
            return 1
        else:
            return 0
    
    def erwartungswert(self):
        return (self.n * self.p)

    def varianz(self):
        return (self.n * self.p * self.q)

    def standardabweichung(self):
        return (math.sqrt(self.varianz()))

if __name__ == "__main__":
    binominal = Bin(5, 0.25)
    print("P(X = 2):", binominal.pdf(2))
    print("P(X <= 5):", binominal.cdf(3))
    print("Erwartungswert:", binominal.erwartungswert())
    print("Varianz:", binominal.varianz())
    print("Standardabweichung:", binominal.standardabweichung())

    