

import numpy as np
from scipy.stats import binom


# "Spot" is going to be a vector, "Strike" is going to be a scalar
# This is vectorizing the payoff function
def CallPayOff(Spot, Strike):
    return np.maximum(Spot - Strike, 0.0)


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
        callT += CallPayOff(spotT, X) * binom.pmf(numSteps - i, numSteps, pu)
    callPrice = callT * np.exp(-r * T)
    return callPrice


def main():
    S = 41
    X = 40
    r = 0.08
    T = 1
    N = 3
    beta = 0.0
    sigma = 0.30
    # u = 1.2
    # d = 0.8

    callPrice = EuropeanBinomial(S, X, r, beta, sigma, T, N)
    print("The N-Period European Binomial Price is = {0:.4f}".format(callPrice))


main()
