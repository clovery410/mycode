from math import sqrt, pow

def square (x):
    return x * x

def sum_of_squares (a, b):
    return add (square (a), square (b))

def distance (x1, y1, x2, y2):
    return sqrt (sum_of_squares (x1 - x2, y1 -y2))
