# Q1. The idea of smoothing a function is an important concept in signal processing. If f is a one-argument function and dx is some small number, then the smoothed version of f is the function whose value at a point x is the average of f(x-dx), f(x), and f(x+dx). Write a funciton smooth that takes as input a function f and a value to use for dx and returns a function that computes the smoothed version of f. Do not use any def statements inside of smooth; use lambda expressions instead.
def smooth(f, dx):
    """Return the smoothed version of f, g where

    g(x) = (f(x - dx) + f(x) + f(x + dx)) / 3

    >>> square = lambda x: x ** 2
    >>> round(smooth(square, 1)(0), 3)
    0.667
    """
    return lambda x: (f(x - dx) + f(x) + f(x + dx)) / 3


# It is sometimes valuable to repeatedly smooth a function (that is, smooth the smoothed function, and so on) to obtain the n-fold smoothed function. Show how to generate the n-fold smoothed function, n_fold_smooth, of any given function using your smooth function and repeated from homework2. As with smooth, use lambda expressions rather than def statements in the body of n_fold_smooth.

def n_fold_smooth(f, dx, n):
    """Return the n-fold smoothed version of f

    >>> square = lambda x: x ** 2
    >>> round(n_fold_smooth(square, 1, 3)(0), 3)
    2.0
    """
    #return smooth(smooth(smooth(f, dx), dx), dx)
    i = 1
    g = f
    while i <= n:
        g = smooth(g, dx)
        i = i + 1
    return g

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
