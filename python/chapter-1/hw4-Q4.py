def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x * x)
    29
    """
    if n == 0:
        return 0
    return term(n, n, odd_term, even_term) + interleaved_sum(n - 1, odd_term, even_term)
    

def term(n, count, odd_term, even_term):
    if count == 0:
        return even_term(n)
    elif count == 1:
        return odd_term(n)
    else:
        return term(n, count - 2, odd_term, even_term)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(interleaved_sum(7, lambda x: x + 1, lambda x: x * 2))
