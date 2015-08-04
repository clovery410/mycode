"""2. Now, what if we wanted to print a sequence of primes up to the nth prime. What would be a simple way to do this?
"""
def nth_prime(n):
    i, x = 0, 1
    while i < n:
        i = i + 1
        x = x + 1
        while not is_prime(x):
            x = x + 1
        print(x)

def is_prime(n):
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

result = nth_prime(10)
