import math
import numpy as np
import matplotlib.pyplot as plt
from copy import copy, deepcopy

class TDMA(object):
    def __init__(self, n):
        self.temperature = [[0.5 for x in range(n)] for x in range(n)]
        self.tolerance = 0.000001
        self.n = n
        self.h = 1.0 / (n - 1)
        
    def TDMASolver(self, a, b, c, r, idx, lamda, direction):
        temperature = self.temperature
        u = [0 for x in range(self.n)]
        
        # only solve interior grid points
        c[1] /= b[1]
        r[1] /= b[1]
        for i in range(2, self.n-1):
            temp = b[i] - a[i] * c[i-1]
            c[i] = c[i] / temp
            r[i] = (r[i] - a[i] * r[i-1]) / temp

        # get last point of interior points
        u[-2] = r[-2]

        # get remaining interior points backward
        for i in reversed(range(1, self.n-2)):
            u[i] = r[i] - u[i+1] * c[i]

        # do the sor relax for interior points calculated by TDMA Line iteration
        if direction == 0:
            for i in range(1, self.n-1):
                temperature[idx][i] = lamda * u[i] + (1 - lamda) * temperature[idx][i]
        else:
            for j in range(1, self.n-1):
                temperature[j][idx] = lamda * u[j] + (1 - lamda) * temperature[j][idx]
                
        
    def getResidual(self, Q, beta):
        temperature = self.temperature

        # initialize residual
        residual = [[0.0 for x in range(self.n)] for x in range(self.n)]
        
        # interior residual
        for j in range(1, self.n-1):
            for i in range(1, self.n-1):
                residual[j][i] = (temperature[j][i+1] + temperature[j][i-1] + beta * beta * temperature[j+1][i] + beta * beta * temperature[j-1][i] - (2 + 2 * beta * beta) * temperature[j][i]) / (self.h * self.h)

        # top and bottom residual
        for i in range(1, self.n-1):
            residual[0][i] = (3 * temperature[0][i] - 4 * temperature[1][i] + temperature[2][i]) / (2 * self.h)
            residual[-1][i] = (-3 * temperature[-1][i] + 4 * temperature[-2][i] - temperature[-3][i]) / (2 * self.h) - Q
        
        res = math.sqrt(sum(x*x for elem in residual for x in elem) / ((self.n - 2) * self.n))
        return res

    def TwoDHeatSteady(self, lamda):
        temperature = self.temperature
        rms = []
        beta = 0.67
        Q = (-1 * 10**6 * 0.15) / (50.2 * 100)
        direction = 0  # direction has 2 values, 0 means sweep along j, 1 means sweep along i
        
        # set boundry
        for j in range(self.n):
            temperature[j][0] = temperature[j][-1] = 1
        
        res = self.getResidual(Q, beta)
        rms.append(math.log10(res))

        # start iteration
        count = 0
        while res >= self.tolerance:
            for idx in reversed(range(1, self.n-1)):
                b = [-2 * (1 + beta * beta)] * self.n
                if direction == 0:  # Initial a, c and r when doing sweeping up
                    a, c = [1] * self.n, [1] * self.n
                    r = [-beta * beta * (temperature[idx-1][i] + temperature[idx+1][i]) for i in range(self.n)]
                    r[1] -= 1
                    r[-2] -= 1
                else:  # Initial a, c and r when doing sweeping right
                    a, c = [beta *beta] * self.n, [beta * beta] * self.n
                    r = [-temperature[j][idx+1] - temperature[j][idx-1] for j in range(self.n)]
                    r[1] -= beta * beta * temperature[0][idx]
                    r[-2] -= beta * beta * temperature[-1][idx]
                
                self.TDMASolver(a, b, c, r, idx, lamda, direction)

            # solove boundry
            for i in range(1, self.n-1):
                # top
                temperature[0][i] = (4 * temperature[1][i] - temperature[2][i]) / 3
                # bottom
                temperature[-1][i] = (4 * temperature[-2][i] - temperature[-3][i] - 2 * self.h * Q) / 3

            if direction == 1:
                res = self.getResidual(Q, beta)
                count += 1
                rms.append(math.log10(res))
                
            direction ^= 1

        return rms, count

if __name__ == "__main__":
    for lamda in [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.99]:
        tdma = TDMA(21)
        temp, res = tdma.TwoDHeatSteady(lamda)
        print "iteration count for lamda = " + str(lamda) + " is: " + str(res)
        
    # tdma = TDMA(21)
    # print "iteration count for lambda = 1.2 is: " + str(tdma.TwoDHeatSteady(1.2)[1])
    # # print tdma.temperature
    # x_line = [tdma.temperature[j][6] for j in range(21)][::-1]
    # y_line = tdma.temperature[6]

    # plt.xlabel('Grid point along the line')
    # plt.ylabel('temperature')
    # plt.title('Dimensionless temperature along the line x = 0.03 and line y = 0.105')
    # plt.plot(x_line, 'b', label = 'Along line x = 0.03 m')
    # plt.plot(y_line, 'r', label = 'Along line y = 0.105 m')
    # plt.legend()
    # plt.ylim(ymin = 0)

    # # plt.xlabel('x')
    # # plt.ylabel('temperature')
    # # plt.title('Dimensionless temperature along the line y = 0.105')
    # # plt.plot(y_line)
    # # plt.ylim(ymin = 0)

    # plt.show()
