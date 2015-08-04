from operator import add, mul
def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.
    
    >>> a = hailstone(10) #Seven elements are 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    count = 1 #initial counting number count is 0
    while True:
        print (n)
        if n == 1:
            return count
        n = n * 3 + 1 if n % 2 else n // 2
        count = count + 1            
            
    # while n != 1:
    #     print (n)
    #     count = count + 1
    #     if n%2:
    #         n = add(mul(n, 3), 1)
    #     else:
    #         n = n // 2
    # print (n)
    # return count

#result = hailstone(10)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
