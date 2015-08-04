# Write sum_primes_up_to(n), which sums up every prime up to and including n. Assume you have an isprime() predicate.
def sum_primes_up_to(n):
    """
    >>> sum_primes_up_to(10)
    17
    >>> sum_primes_up_to(20)
    77
    """
    if n == 1:
        return 0
    elif isprime(n):
        return sum_primes_up_to(n - 1) + n
    else:
        return sum_primes_up_to(n - 1)
        
def isprime(n):
    count = 2
    while count < n:
        if n % count == 0:
            return False
        count += 1
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
