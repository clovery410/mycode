from fractions import gcd

class Rational(object):
    """A mutable fraction.
    >>> f = Rational(3, 5)
    >>> f
    Rational(3, 5)
    >>> print(f)
    3/5
    >>> f.float_value
    0.6
    >>> f.numerator = 4
    >>> f.float_value
    0.8
    >>> f.denominator -= 3
    >>> f.float_value
    2.0
    """

    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numerator = numer // g
        self.denominator = denom // g
        
    @property
    def float_value(self):
        return self.numerator / self.denominator

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numerator, self.denominator)

    def __str__(self):
        return '{0}/{1}'.format(self.numerator, self.denominator)
    
    def __add__(self, num):
        return add_rational(self, num)

    def __mul__(self, num):
        return mul_rational(self, num)

    def __eq__(self, num):
        return eq_rational(self, num)

    def __bool__(self):
        return self.numerator != 0

def add_rational(r1, r2):
    denom = r1.denominator * r2.denominator
    numer1 = r1.numerator * r2.denominator
    numer2 = r1.denominator * r2.numerator
    return Rational(numer1 + numer2, denom)

def mul_rational(r1, r2):
    return Rational(r1.numerator * r2.numerator, r1.denominator * r2.denominator)

def eq_rational(r1, r2):
    return (r1.numerator * r2.denominator == r2.numerator * r1.denominator)

class ImmutableRational(Rational):
    """An immutable fraction
    >>> f = ImmutableRational(3, 5)
    >>> f
    ImmutableRational(3, 5)
    >>> f.numerator = 4
    >>> f
    ImmutableRational(3, 5)
    >>> f.denominator -= 3
    >>> f
    ImmutableRational(3, 5)
    """
    def __init__(self, numer, denom):
        Rational.__init__(self, numer, denom)
        self.finalized = True

    def __setattr__(self, attr, value):
        if hasattr(self, 'finalized') and self.finalized:
            return 
        object.__setattr__(self, attr, value)

    def __repr__(self):
        return 'ImmutableRational({0}, {1})'.format(self.numerator, self.denominator)


def mutate_rational(r):
    """Mutate a rational by adding one to its denominator.
    >>> f = ImmutableRational(3, 5)
    >>> f
    ImmutableRational(3, 5)
    >>> mutate_rational(f)
    >>> f
    ImmutableRational(3, 6)
    """
    new_denom = r.denominator + 1
    dict2 = {'denominator': new_denom}
    r.__dict__.update(dict2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
