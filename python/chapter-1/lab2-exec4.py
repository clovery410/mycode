def cycle(f1, f2, f3):
    """ Return a function that is itself a higher order function
    >>> add1 = lambda x: x + 1
    >>> times2 = lambda x: 2 * x
    >>> add3 = lambda x: x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def h(_n):
        def run_cycle(x):
            n = _n
           
            while n >= 0:
                if n == 0:
                    return x

                if n > 0:
                    x = f1(x)
                    n = n - 1
                else:
                    return x

                if n > 0:
                    x = f2(x)
                    n = n - 1
                else:
                    return x

                if n > 0:
                    x = f3(x)
                    n = n - 1
                else:
                    return x
        
        return run_cycle
    return h

def cycle_n(f1, f2, f3):
    def ret_fn(n):
        def ret(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                else:
                    x = f3(x)
                i = i + 1
            return x
        return ret
    return ret_fn

if __name__ == "__main__":
    import doctest
    doctest.testmod()

            # n = 0, return x
            # n = 1, return f1(x)
            # n = 2, return f2(f1(x))
            # n = 3, return f3(f2(f1(x)))
            # n = 4, return f1(f3(f2(f1(x))))
