import math
import numpy as np
import matplotlib.pyplot as plt
from copy import copy, deepcopy

def getResidual(curr_temp, h):
    # initialize residual
    res, n = 0.0, len(curr_temp)
    residual = [[0.0 for x in range(n)] for x in range(n)]
    
    for j in range(1, n-1):
        for i in range(1, n-1):
            residual[j][i] = (curr_temp[j+1][i] + curr_temp[j-1][i] + curr_temp[j][i+1] + curr_temp[j][i-1] - 4 * curr_temp[j][i]) / (h * h)
            
    return math.sqrt(sum(x*x for elem in residual for x in elem) / ((n-2)*(n-2)))
    
def jacobi(h, initial_temp, tolerance):
    n = int(1 / h) + 1
    rms = []
    
    # initialize temperature
    curr_temp = [[initial_temp for x in range(n)] for x in range(n)]
    
    # set boundry
    for j in range(n):
        curr_temp[j][0] = curr_temp[j][n-1] = 1.0
       
    for i in range(n):
        curr_temp[0][i] = curr_temp[n-1][i] = 0.0

    res = getResidual(curr_temp, h)
    rms.append(math.log10(res))

    # start iteration
    count = 0
    while res >= tolerance:
        prev_temp = deepcopy(curr_temp)
        for j in range(1, n-1):
            for i in range(1, n-1):
                curr_temp[j][i] = (prev_temp[j+1][i] + prev_temp[j-1][i] + prev_temp[j][i+1] + prev_temp[j][i-1]) / 4.0
        res = getResidual(curr_temp, h)
        count += 1
        rms.append(math.log10(res))

    return rms

def gauss_seidel(h, initial_temp, tolerance):
    n = int(1 / h) + 1
    rms = []
    
    # initialize temperature
    curr_temp = [[initial_temp for x in range(n)] for x in range(n)]
    
    # set boundry
    for j in range(n):
        curr_temp[j][0] = curr_temp[j][n-1] = 1.0
       
    for i in range(n):
        curr_temp[0][i] = curr_temp[n-1][i] = 0.0

    res = getResidual(curr_temp, h)
    rms.append(math.log10(res))

    # start iteration
    count = 0
    while res >= tolerance:
        prev_temp = deepcopy(curr_temp)
        for j in range(1, n-1):
            for i in range(1, n-1):
                curr_temp[j][i] = (prev_temp[j+1][i] + curr_temp[j-1][i] + prev_temp[j][i+1] + curr_temp[j][i-1]) / 4.0
        res = getResidual(curr_temp, h)
        count += 1
        rms.append(math.log10(res))

    return rms

def sor(h, initial_temp, tolerance, lamda):
    n = int(1 / h) + 1
    rms = []
    
    # initialize temperature
    curr_temp = [[initial_temp for x in range(n)] for x in range(n)]
    
    # set boundry
    for j in range(n):
        curr_temp[j][0] = curr_temp[j][n-1] = 1.0
       
    for i in range(n):
        curr_temp[0][i] = curr_temp[n-1][i] = 0.0

    res = getResidual(curr_temp, h)
    rms.append(math.log10(res))
    
    # start iteration
    count = 0
    while res >= tolerance:
        prev_temp = deepcopy(curr_temp)
        for j in range(1, n-1):
            for i in range(1, n-1):
                curr_temp[j][i] = (prev_temp[j+1][i] + curr_temp[j-1][i] + prev_temp[j][i+1] + curr_temp[j][i-1]) / 4.0 * lamda + (1 - lamda) * prev_temp[j][i]

        res = getResidual(curr_temp, h)
        count += 1
        rms.append(math.log10(res))
        
    return rms

jacobi_rms = jacobi(0.05, 0.5, 0.000001)
gauss_rms = gauss_seidel(0.05, 0.5, 0.000001)
sor1_rms = sor(0.05, 0.5, 0.000001, 1.2)
sor2_rms = sor(0.05, 0.5, 0.000001, 1.9)

# jacobi_temp = jacobi(0.05, 0.3, 0.00000001)
# jacobi_fix_x = [elem[6] for elem in jacobi_temp]
# gauss_temp = gauss_seidel(0.05, 0.3, 0.00000001)
# gauss_fix_x = [elem[6] for elem in gauss_temp]
# sor1_temp = sor(0.05, 0.3, 0.00000001, 1.2)
# sor1_fix_x = [elem[6] for elem in sor1_temp]
# sor2_temp = sor(0.05, 0.3, 0.00000001, 1.9)
# sor2_fix_x = [elem[6] for elem in sor2_temp]

y_line = np.array([1.000e+00, 8.909e-01, 7.879e-01, 6.957e-01, 6.167e-01, 5.516e-01, 5.000e-01, 4.611e-01, 4.339e-01, 4.180e-01, 4.127e-01, 4.180e-01, 4.339e-01, 4.611e-01, 5.000e-01, 5.516e-01, 6.167e-01, 6.957e-01, 7.879e-01, 8.909e-01, 1.000e+00])

x_line = np.array([0.000e+00, 1.091e-01, 2.121e-01, 3.043e-01, 3.833e-01, 4.484e-01, 5.000e-01, 5.389e-01, 5.661e-01, 5.820e-01, 5.873e-01, 5.820e-01, 5.661e-01, 5.389e-01, 5.000e-01, 4.484e-01, 3.833e-01, 3.043e-01, 2.121e-01, 1.091e-01, 8.592e-17])

# plt.xlabel('x')
# plt.ylabel('theta')
# plt.title('Analytical - Dimensionless temperature along the line y = 0.7')
# plt.plot(y_line)
# plt.ylim(ymin = 0)

# plt.xlabel('x')
# plt.ylabel('theta (initial = 0.3, tolerance = 10e-8)')
# plt.title('Jacobi - Dimensionless temperature along the line y = 0.7')
# plt.plot(jacobi_temp[6], 'k', label = 'Jacobi solution')
# plt.plot(y_line, 'bo', label = 'Analytical solution')
# plt.legend(loc = 4)
# plt.ylim(ymin = 0)

# plt.xlabel('x')
# plt.ylabel('theta (initial = 0.3, tolerance = 10e-8)')
# plt.title('Gauss - Dimensionless temperature along the line y = 0.7')
# plt.plot(gauss_temp[6], 'k', label = 'Gauss-seidel solution')
# plt.plot(y_line, 'bo', label = 'Analytical solution')
# plt.legend(loc = 4)
# plt.ylim(ymin = 0)

# plt.xlabel('x')
# plt.ylabel('theta (initial = 0.3, tolerance = 10e-8)')
# plt.title('SOR 1.9 - Dimensionless temperature along the line y = 0.7')
# plt.plot(sor2_temp[6], 'k', label = 'SOR 1.9 solution')
# plt.plot(y_line, 'bo', label = 'Analytical solution')
# plt.legend(loc = 4)
# plt.ylim(ymin = 0)

# plt.xlabel('y')
# plt.ylabel('theta (initial = 0.3)')
# plt.title('Analytical - Dimensionless temperature along the line x = 0.3')
# plt.plot(x_line)
# plt.ylim(ymin = 0)

# plt.xlabel('y')
# plt.ylabel('theta (initial = 0.3, tolerance = 10e-6)')
# plt.title('Jacobi - Dimensionless temperature along the line x = 0.3')
# plt.plot(jacobi_fix_x, 'k', label = 'Jacobi solution')
# plt.plot(x_line, 'bo', label = 'Analytical solution')
# plt.legend(loc = 4)
# plt.ylim(ymin = 0)

# plt.xlabel('y')
# plt.ylabel('theta (initial = 0.3, tolerance = 10e-6)')
# plt.title('Gauss - Dimensionless temperature along the line x = 0.3')
# plt.plot(gauss_fix_x, 'k', label = 'Gauss-seidel solution')
# plt.plot(x_line, 'bo', label = 'Analytical solution')
# plt.legend(loc = 4)
# plt.ylim(ymin = 0)

# plt.xlabel('y')
# plt.ylabel('theta (initial = 0.3, tolerance = 10e-6)')
# plt.title('SOR 1.2 - Dimensionless temperature along the line x = 0.3')
# plt.plot(sor1_fix_x, 'k', label = 'SOR 1.2 solution')
# plt.plot(x_line, 'bo', label = 'Analytical solution')
# plt.legend(loc = 4)
# plt.ylim(ymin = 0)

# for i in range(len(jacobi_temp)):
#     print sor2_rms[i+1] - sor2_rms[i]

plt.xlabel('iteration counts')
plt.ylabel('log10(RMS)')
plt.title('Residual Equation - with h = 0.05 plot')
plt.plot(jacobi_rms, 'b', label = 'Jacobi')
plt.plot(gauss_rms, 'r', label = 'Gauss-seidel')
plt.plot(sor1_rms, 'g', label = 'SOR 1.2')
plt.plot(sor2_rms, 'y', label = 'SOR 1.9')
plt.legend()

plt.show()        
# print "jacobi method with h = 0.1: " + str(jacobi(0.1, 0.5, 0.000001)) + " iterations.\n"
# print "jacobi method with h = 0.05: " + str(jacobi(0.05, 0.5, 0.000001)) + " iterations.\n"
# print "gauss_seidel method with h = 0.1: " + str(gauss_seidel(0.1, 0.5, 0.000001)) + " iterations.\n"
# print "gauss_seidel method with h = 0.05: " + str(gauss_seidel(0.05, 0.5, 0.000001)) + " iterations.\n"
# print "sor method with h = 0.1 and lamda = 1.2: " + str(sor(0.1, 0.5, 0.000001, 1.2)) + " iterations.\n"
# print "sor method with h = 0.1 and lamda = 1.9: " + str(sor(0.1, 0.5, 0.000001, 1.9)) + " iterations.\n"
# print "sor method with h = 0.05 and lamda = 1.2: " + str(sor(0.05, 0.5, 0.000001, 1.2)) + " iterations.\n"
# print "sor method with h = 0.05 and lamda = 1.9: " + str(sor(0.05, 0.5, 0.000001, 1.9)) + " iterations.\n"
    
                
                
