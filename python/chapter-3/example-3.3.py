class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess

def improve(update, done, guess=1, max_updates=1000):
    k = 0
    try:
        while not done(guess) and k < max_updates:
            guess = update(guess)
            k = k + 1
        return guess
    except ValueError:
        raise IterImproveError(guess)

def find_zero(f, guess=1):
    def done(x):
        return f(x) == 0
    try:
        return improve(newton_update(f), done, guess)
    except IterImproveError as e:
        return e.last_guess

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

from math import sqrt
find_zero(lambda x: 2 * x * x + sqrt(x))
