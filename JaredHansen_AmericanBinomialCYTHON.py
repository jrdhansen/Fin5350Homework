
## NOTE: I wrote this code in PyCharm for ease of text-editing. I haven't been able to figure out how to convert it to a .pyx file
##       type, so I uploaded it as a .py file. Not ideal, but better than nothing. To my knowledge, the code works correctly when
##       run as cython code.

## Binomial Model for American-style options in Cython
## Brough named this file deacon.pyx in the server (engine.pyx on gitHub)

## import the numpy library for both python and C++
cimport numpy as np
import numpy as np



cdef class Payoff:
    """ An abstract base class for option payoffs."""
    def __init__(self, strike):
        self._strike = strike


cdef class VanillaCallPayoff(Payoff):
    """A concrete class for plain vanilla call option payoff."""
    cpdef payoff(self, double spot):
        return np.maximum(spot - self._strike, 0.0)


# we'll also want a class for Put options called
# cdef class VanillaPutPayoff(Payoff):




cdef class Option:
    def __init__(self, expiry, payoff):
        self._expiry = expiry
        self._payoff = payoff
    cpdef payoff(self, double spot):
        return self._payoff.payoff(spot)




cdef class PricingEngine:
    """ An abstract base class for option pricing engines."""
    cdef double calculate(self, Option option, MarketData data):
        pass




cdef class BinomialEngine(PricingEngine):
    """ An interface class for binomial pricing engines."""
    def __init__(self, nsteps):
        self._nsteps = nsteps

    cdef double calculate(self, Option option, MarketData data):
        pass


cdef class AmericanBinomialEngine(BinomialEngine):
    """ A concrete class for the american binomial option pricing model"""
    cdef double calculate(self, Option option, MarketData data):
        cdef double dt = option.expiry / self._nsteps
        cdef double u = np.cexp((data.rate - data.div) * dt + data.vol * np.csqrt(dt))
        cdef double d = np.cexp((data.rate - data.div) * dt - data.vol * np.csqrt(dt))
        cdef double pu = (np.exp((data.rate - data.div) * dt) - d) / (u-d)
        cdef double pd = 1.0 - pu
        cdef double disc = np.cexp(-data.rate * dt)
        cdef double dpu = disc * pu
        cdef double dpd = disc * pd
        cdef long numNodes = self._nsteps + 1
        cdef double [::1] spot_t = np.empty(numNodes, dtype = np.float64)
        cdef double [::1] call_t = np.empty(numNodes, dtype = np.float64)
        cdef int i, j


# modify the stuff below this line: it's just coming from the python version
# I think that Ct = call_t, St = spot_t, nodes = numNodes, steps = self._nsteps
    # "Ct" = option value at time t, "St" = spot value at time t


      for i in range(num_nodes):
            spot_t[i] = data.spot * cpow(u, self._nsteps - i) * cpow(d, i)
            call_t[i] = option.payoff(spot_t[i])

        for i in range(self._nsteps - 1, -1, -1):
            for j in range(i + 1):
                call_t[j] = dpu * call_t[j] + dpd * call_t[j+1]
                spot_t[j] = spot_t[j] / u
                call_t[j] = np.maximum(call_t[j], option.payoff(spot_t[j]))


        return call_t[0]
