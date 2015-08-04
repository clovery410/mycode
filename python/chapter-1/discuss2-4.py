"""Suppose we would like to square or double every natural number from 1 to n and print the result as we go. Using the functions square and double, each of which are functions that take one argument that do as their name imply, fill out the following:"""

def square_every_number(n):
    every(square, n)

def double_every_number(n):
    every(double, n)

def every(f, n):
    x = 1
    while x <= n:
        print(f(x))
        x += 1

def square(x):
    return x * x

def double(x):
    return 2 * x

result1 = square_every_number(10)
result2 = double_every_number(10)
