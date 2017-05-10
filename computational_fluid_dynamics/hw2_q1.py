import pprint
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.linalg

def LUDecomp(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    count = 0
    
    for i in range(n):
        L[i][i] = 1

    for j in range(n):
        for i in range(j+1):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
            count = count + 1 + 2 * i - 1 if i > 0 else count + 1

        for i in range(j+1, n):
            L[i][j] = (A[i][j] - sum(L[i][k] * U[k][j] for k in range(j))) / U[j][j]
            count = count + 2 + 2 * j -1 if j > 0 else count + 2

    # print "A:"
    # pprint.pprint(A)
    
    # print "L:"
    # pprint.pprint(L)

    # print "U:"
    # pprint.pprint(U)

    # print "LU:"
    # pprint.pprint(L.dot(U))

    print "Flops required is: " + str(count)
    return L, U

def LUSolve(A, L, U, r):
    # x = np.linalg.solve(A, r)
    # Ly = r, L is [n x n], y and r is [n x 1]
    # Uu = y
    n = len(L)
    y = np.zeros((n, 1))
    u = np.zeros((n, 1))

    y[0][0] = r[0][0] / L[0][0]
    for i in range(1, n):
        y[i][0] = (r[i][0] - sum(L[i][j] * y[j][0] for j in range(i))) / L[i][i]

    u[-1][0] = y[-1][0] / U[-1][-1]
    for i in reversed(range(n-1)):
        u[i][0] = (y[i][0] - sum(U[i][j] * u[j][0] for j in range(i+1, n))) / U[i][i]

    # print "x is:"
    # pprint.pprint(x)

    return u

A = np.array([[1, 2, 4, 8, 16],
              [3, 5, 12, 22, 40],
              [1, 3, 9, 27, 81],
              [2, 5, 4, 10, 12],
              [1, 4, 2, 6, 4]])
r = np.array([[3],
              [1],
              [5],
              [7],
              [6]])

L, U = LUDecomp(A)
print "Matrix L is: "
pprint.pprint(L)
print "Matrix U is: "
pprint.pprint(U)
res = LUSolve(A, L, U, r)
print "u's result is: "
pprint.pprint(res)
    

