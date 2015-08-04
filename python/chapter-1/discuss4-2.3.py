#3. The TAs want to print handouts for their students. However, for some unfathomable reason, both the priters are broken; the first printer only prints multiples of n1, and the second printer only prints multiples of n2. Help the TAs figure out whether or not it is possible to print an exact number of handouts!
def hasSum(sum, n1, n2):
    """
    >>> hasSum(1, 3, 5)
    False
    >>> hasSum(5, 3, 5) # 1(5) + 0(3) = 5
    True
    >>> hasSum(11, 3, 5) # 2(3) + 1(5) = 11
    True
    """
    if sum == 0:
        return True
    elif sum < 0:
        return False
    else:
        return hasSum(sum - n1, n1, n2) or hasSum(sum - n2, n1, n2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
