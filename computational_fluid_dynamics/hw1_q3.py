import numpy as np
import matplotlib.pyplot as plt

def exact_deriv():
    return np.exp(1) - np.exp(-1)

def f(x):
    return np.exp(x) + np.exp(-x)

def first_forward(h):
    return (f(1+h) - f(1)) / h

def first_3symmetric(h):
    return (f(1+h) - f(1-h)) / (2 * h)

def first_5symmetric(h):
    return (f(1-2*h) - 8*f(1-h) + 8*f(1+h) - f(1+2*h)) / (12 * h)

def second_3asymmetric(h):
    return (f(1) - 2*f(1+h) + f(1+2*h)) / (h**2)

def second_3symmetric(h):
    return (f(1+h) - 2*f(1) + f(1-h)) / (h**2)

def second_5symmetric(h):
    return (-f(1-2*h) + 16*f(1-h) -30*f(1) + 16*f(1+h) - f(1-2*h)) / (12 * h**2)

h_val = np.array([0.25, 0.25/2, 0.25/4, 0.25/8, 0.25/16, 0.25/32, 0.25/64, 0.25/2**7, 0.25/2**8, 0.25/2**9, 0.25/2**10], dtype=np.float64)

# plt.xlabel('log10h')
# plt.ylabel('log10E')
# plt.title('First Derivative - Forward difference form')
# plt.plot(np.abs(np.log10(h_val)), np.abs(np.log10(np.abs(first_forward(h_val) / exact_deriv() - 1))))

plt.xlabel('log10h')
plt.ylabel('log10E')
plt.title('First Derivative - 3 point symmetric form')
plt.plot(np.abs(np.log10(h_val)), np.abs(np.log10(np.abs(first_3symmetric(h_val) / exact_deriv() - 1))))

# plt.xlabel('log10h')
# plt.ylabel('log10E')
# plt.title('First Derivative - 5 point symmetric form')
# plt.plot(np.abs(np.log10(h_val)), np.abs(np.log10(np.abs(first_5symmetric(h_val) / exact_deriv() - 1))))

# plt.xlabel('log10h')
# plt.ylabel('log10E')
# plt.title('Second Derivative - 3 point asymmetric form')
# plt.plot(np.abs(np.log10(h_val)), np.abs(np.log10(np.abs(second_3asymmetric(h_val) / exact_deriv() - 1))))

# plt.xlabel('log10h')
# plt.ylabel('log10E')
# plt.title('Second Derivative - 3 point symmetric form')
# plt.plot(np.abs(np.log10(h_val)), np.abs(np.log10(np.abs(second_3symmetric(h_val) / exact_deriv() - 1))))

# plt.xlabel('log10h')
# plt.ylabel('log10E')
# plt.title('Second Derivative - 5 point symmetric form')
# plt.plot(np.abs(np.log10(h_val)), np.abs(np.log10(np.abs(second_5symmetric(h_val) / exact_deriv() - 1))))

# plt.xlabel('|log10h|')
# plt.ylabel('|log10|TE||')
# plt.title('Leading order TE for First Derivative i)')
# plt.plot(np.abs(np.log10(h_val)), np.abs(np.log10(np.abs(first_3symmetric(h_val) - first_forward(h_val)))))

# plt.xlabel('|log10h|')
# plt.ylabel('|log10|TE||')
# plt.title('Leading order TE for First Derivative ii)')
# plt.plot(np.abs(np.log10(h_val)), np.abs(np.log10(np.abs(first_5symmetric(h_val) - first_3symmetric(h_val)))))

# plt.xlabel('|log10h|')
# plt.ylabel('|log10|TE||')
# plt.title('Leading order TE for Second Derivative i)')
# plt.plot(np.abs(np.log10(h_val)), np.abs(np.log10(np.abs(second_3symmetric(h_val) - second_3asymmetric(h_val)))))

# plt.xlabel('|log10h|')
# plt.ylabel('|log10|TE||')
# plt.title('Leading order TE for Second Derivative ii)')
# plt.plot(np.abs(np.log10(h_val)), np.abs(np.log10(np.abs(second_5symmetric(h_val) - second_3symmetric(h_val)))))

plt.show()
