"""Using the is_prime function, fill in the following function, which generates the nth prime number. For example, the 2nd prime number is 3, the 5th prime number is 11, and so on.
"""
def nth_prime(n):
    count, curr = 1, 2
    while count < n:
        curr = curr + 1
        if is_prime(curr):
            count = count + 1
    return curr

def is_prime(n):
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

print(nth_prime(2))
print(nth_prime(3))
print(nth_prime(4))
print(nth_prime(5))
print(nth_prime(6))
