import pdb
import numpy as np
import scipy as sp
import scipy.linalg
from fractions import Fraction

def getResidual(v1, v2):
    _sum = 0
    for i in range(len(v2)):
        _sum += abs(v1[i] - v2[i])
    return _sum
    
def solveVector(init_v, A, v_prime):
#    print A
    curr_v = np.dot(A, init_v)
    count = 0
    while getResidual(curr_v, init_v) > 0.00001:
        if count <= 5:
            print 'Loop ' + str(count)
            print curr_v
        # pdb.set_trace()
        init_v = curr_v
        curr_v = np.dot(A, init_v) + v_prime
        count += 1

    return curr_v

if __name__ == "__main__":
    # v0 = np.array([Fraction(1,3), Fraction(1,3), Fraction(1,3)])
    # M = np.array([[Fraction(1,3), Fraction(0), Fraction(0)], [Fraction(1,3), Fraction(0), Fraction(1,2)], [Fraction(1,3), Fraction(1), Fraction(1,2)]])
    # N = np.array([[Fraction(1,3), Fraction(1,3), Fraction(1,3)], [Fraction(1,3), Fraction(1,3), Fraction(1,3)], [Fraction(1,3), Fraction(1,3), Fraction(1,3)]])
    # A = Fraction(4,5) * M + Fraction(1,5) * N
    v0 = np.array([Fraction(0), Fraction(1), Fraction(0), Fraction(0)])
    M = np.array([[Fraction(0), Fraction(2,5), Fraction(4,5), Fraction(0)], [Fraction(4,15), Fraction(0), Fraction(0), Fraction(2,5)], [Fraction(4,15), Fraction(0), Fraction(0), Fraction(2,5)], [Fraction(4,15), Fraction(2,5), Fraction(0), Fraction(0)]])
    v_prime = np.array([0, Fraction(1,5), 0, 0])
    print M
    res = solveVector(v0, M, v_prime)
    for num in res:
        print float(num)
