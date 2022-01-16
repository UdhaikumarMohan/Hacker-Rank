import numpy as np
from functools import reduce
b = [24,36]

def GCD(b):

    return(np.gcd.reduce(b))

print(GCD(b))

