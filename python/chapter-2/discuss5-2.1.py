from math import pow

def rational_pow(x, e):
    return rational(pow(numer(x), e), pow(denom(x), e))
