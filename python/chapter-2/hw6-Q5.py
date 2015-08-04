def pizza_sort(lst):
    """Perform an in-place pizza sort on the given list, resulting in elements in descending order.

    >>> a = [8, 5, 7, 3, 1, 9, 2]
    >>> pizza_sort(a)
    >>> a
    [9, 8, 7, 5, 3, 2, 1]
    """
    def help_func(lst, i):
        if i == len(lst) - 1:
            return lst
        else:
            tem1 = lst[i]
            tem2 = index_largest(lst[i:]) + i
            lst[i] = lst[index_largest(lst[i:]) + i]
            lst[tem2] = tem1
            return help_func(lst, i+1)
        return help_func
    help_func(lst, i=0)
    

def index_largest(seq):
    assert len(seq) > 0
    max_i = 0
    max_elem = seq[0]
    for i in range(len(seq)):
        if seq[i] > max_elem:
            max_elem = seq[i]
            max_i = i
    return max_i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
