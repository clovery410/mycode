def iterative_continued_frac(n_term, d_term, k):
    """Return the k-term continued fraction with numerators defined by n_term and denominators defined by d_term.

    >>> # golden ratio
    ... round(iterative_continued_frac(lambda x: 1, lambda x: 1, 8), 3)
    0.618
    >>> # 1 / (1 + (2 / (2 + (3 / (3 + (4 / 4))))))
    ... round(iterative_continued_frac(lambda x: x, lambda x: x, 4), 6)
    0.578947
    """
    i = k
    d = n_term(i) / d_term(i)
    if i == 1:
        return d
    while i > 1:
        d = d + d_term(i - 1)
        n = n_term(i - 1)
        d = n / d
        i = i - 1
    return d

def recursive_continued_frac(n_term, d_term, k):
    """Return the k-term continued fraction with numerators defined by n_term and denominators defined by d_term.

    >>> # golden ratio
    ... round(recursive_continued_frac(lambda x: 1, lambda x: 1, 8), 3)
    0.618
    >>> # 1 / (1 + (2 / (2 + (3 / (3 + (4 / 4))))))
    ... round(recursive_continued_frac(lambda x: x, lambda x: x, 4), 6)
    0.578947
    """
    def cal_d(n_term, d_term, i, n):
        if i == n:
            return n_term(i) / d_term(i)
        else:
            return n_term(i) / (d_term(i) + cal_d(n_term, d_term, i+1, n))
    return cal_d(n_term, d_term, 1, k)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
