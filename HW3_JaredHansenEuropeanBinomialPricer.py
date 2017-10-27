

import numpy as np
from scipy.stats import binom




class VanillaPayoff(object):
    def __init__(self, strike, expiry):
        self.strike = strike
        self.expiry = expiry
        
    def value(self):
        pass
    
class VanillaCallPayoff(VanillaPayoff):
    def value(self, spot):
        return np.maximum(spot - self.strike, 0.0)
    
class VanillaPutPayoff(VanillaPayoff):
    def value(self, spot):
        return np.maximum(self.strike - spot, 0.0)


# Prices options with the European Binomial model
# strike price, spot price, risk free rate, up, down, T
def EuropeanBinomial(S, X, r, beta, sigma, T, N):
    # number of steps in the tree
    H = T / N
    numSteps = N
    numNodes = numSteps + 1
    spotT = 0.0
    callT = 0.0
    u = np.exp((r - beta) * H + sigma * (np.sqrt(H)))
    d = np.exp((r - beta) * H - sigma * (np.sqrt(H)))  # risk neutral probability
    pu = (np.exp((r - beta) * H) - d) / (u - d)
    pd = 1 - pu
    for i in range(numNodes):
        spotT = S * (u ** (numSteps - i)) * (d ** (i))
        callT += option.value(spotT) * binom.pmf(numSteps - i, numSteps, pu)
    callPrice = callT * np.exp(-r * T)
    return callPrice


def main():
    S = 41
    X = 40
    T = 1
    option = VanillaCallPayoff(X, T)
    r = 0.08
    N = 3
    beta = 0.0
    sigma = 0.30
    # u = 1.2
    # d = 0.8

    callPrice = EuropeanBinomial(S, X, r, beta, sigma, T, N)
    print("The N-Period European Binomial Price is = {0:.4f}".format(callPrice))


main()
