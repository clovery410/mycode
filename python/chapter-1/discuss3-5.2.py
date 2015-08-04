# 2. Newton's method converges very slowly (or not at all) if the algorithm happens to land on a point where the derivative is very small. Modify the implementation that uses iter_improve to return None if the derivative is under some threshold, say 0.001.
def newtons_method2(fn, guess=1, max_iterations=100):
    def newtons_update(guess, min_size=0.001):
        dtv = derivative(fn, guess)
        if abs(dtv) < min_size:
            return None
        else:
            return guess - fn(guess) / derivative(fn, guess)
    
    def newtons_done(guess):
        ALLOWED_ERROR_MARGIN = 0.0000001
        if guess == None:
            return True
        return abs(fn(guess)) <= ALLOWED_ERROR_MARGIN

    return iter_improve(newtons_update, newtons_done, guess, max_iterations)

def iter_improve(update, isdone, guess=1, max_iterations=100):
    i = 1
    while not isdone(guess) and i <= max_iterations:
        guess = update(guess)
        i += 1
    return guess

def derivative(fn, x, dx=0.00001):
    return (fn(x + dx) - fn(x)) / dx



