""" 1. Write a function and_add_one that takes a function f as an argument(such that f is a function of one argument). It should return a function that takes one argument, and does the same thing as f, except adds one to result."""
def and_add_one(f):
    def wrapped(x):
        return f(x) + 1
    return wrapped

@and_add_one
def f(x):
    return x * x


print(f(3))


""" 2. Write a function and_add that takes a function f and a number n as arguments. It should return a function that takes one argument, and does the same thing as the function argument, except adds n to the result."""
def  and_add(f, n):
    def wrapped(x):
        return f(x) + n
    return wrapped

def f(x):
    return 3 * x

print(and_add(f(3), 5))
