def part_count(n, current_num):
    if n == 0:
        return 1
    if n < 0 or current_num == 0:
        return 0
    return part_count(n, current_num - 1) + part_count(n - current_num, current_num)

def part(n):
    """Return the number of partitions of positive integer n.
    
    >>> part(5)
    7
    >>> part(10)
    42
    >>> part(15)
    176
    >>> part(20)
    627
    """
    return part_count(n, current_num=n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(part(4))
print(part(6))
