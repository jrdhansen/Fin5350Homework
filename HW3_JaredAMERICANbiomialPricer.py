

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


# "Spot" is going to be a vector, "Strike" is going to be a scalar
# This is vectorizing the payoff function
def CallPayOff(Spot, Strike):
    return np.maximum(Spot - Strike, 0.0)


# Prices options with the European Binomial model
# strike price, spot price, risk free rate, up, down, T
def AmericanBinomial(option, S, r, beta, sigma, N):
    # number of steps in the tree
    T = option.expiry
    X = option.strike
    H = T / N
    numSteps = N
    numNodes = numSteps + 1
    spotT = 0.0
    callT = 0.0
    u = np.exp((r - beta) * H + sigma * (np.sqrt(H)))
    d = np.exp((r - beta) * H - sigma * (np.sqrt(H)))  # risk neutral probability
    pu = (np.exp((r - beta) * H) - d) / (u - d)
    pd = 1 - pu
    discount = np.exp(-r * H)
    discountedPriceUp = pu * discount
    discountedpriceDown = pd * discount
    spotPriceArray = np.zeros(numNodes)
    callValueArray = np.zeros(numNodes)

    for i in range(numNodes):
        spotPriceArray[i] = S * (u ** (numSteps - i)) * (d ** (i))
        callValueArray[i] = option.value(spotPriceArray[i])

    for i in range((numSteps-1), -1, -1):
        for j in range (i+1):
            callValueArray[j] = discountedPriceUp * callValueArray[j] + discountedpriceDown * callValueArray[j+1]
            spotPriceArray[j] = spotPriceArray[j] / u
            callValueArray[j] = np.maximum(callValueArray[j], option.value(spotPriceArray[j]))
    return callValueArray[0]



def main():
    X = 41
    T = 1.0
    option = VanillaCallPayoff(X, T)
    S = 41
    r = 0.08
    N = 3
    beta = 0.0
    sigma = 0.30


    callPrice = AmericanBinomial(option, S, r, beta, sigma, N)
    print("The N-Period American Binomial Price is = {0:.4f}".format(callPrice))


main()
