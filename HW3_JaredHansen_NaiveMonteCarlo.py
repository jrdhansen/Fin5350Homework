## Naive Monte Carlo in a Black-Scholes Economy
## 11/13/2017 (Monday)

import numpy as np



# Set up parameters
S = 41.0
K = 40.0
r = 0.08
v = 0.30 #sigma
T = 1.0
q = 0.0
# where the dividend is q

# setting up an empty array of size 1000000
M = 1000000
spot_t = np.empty((M, ))

# getting 1000 values from a standard normal dist
z = np.random.normal(size=(M,))

# drift
nudt = (r - q - 0.5 * v * v) * T
# diffusion
sigdt = v * np.sqrt(T)


# for i in range(M):
  #  spot_t[i] = S * np.exp(nudt + sigdt * z[i])

# to improve upon the loop above, we'll do the following
spot_t = S * np.exp(nudt + sigdt * z)




def CallPayoff(spot, strike):
    return np.maximum(spot-strike, 0.0)

call_t = CallPayoff(spot_t, K)


expectedOptionPayoffasofExpiry = call_t.mean()

callPrice = np.exp(-r * T) * expectedOptionPayoffasofExpiry





def PutPayoff(spot, strike):
    return np.maximum(strike-spot, 0.0)

put_t = PutPayoff(spot_t, K)
putPrice = np.exp(-r * T) * put_t.mean()


# output either "putPrice" or "callPrice"
putPrice
