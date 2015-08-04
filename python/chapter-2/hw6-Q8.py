# Old version
def count_change(a, coins=(50, 25, 10, 5, 1)):
    if a == 0:
        return 1
    elif a < 0 or len(coins) == 0:
        return 0
    return count_change(a, coin[1:]) + count_change(a - coins[0], coins)

#Version 2.0
def make_count_change():
    """Return a function to efficiently count the number of ways to make change.

    >>> cc = make_count_change()
    >>> cc(500, (50, 25, 10, 5, 1))
    59576
    """
    lst = []
    time = []
    def count_change_lst(a, coins):
        # for elem in lst:
        #    if (a, coins) == elem:
        #        time[lst.index(elem)] += 1
        if a == 0:
            return 
        elif a < 0 or len(coins) == 0:
            return 0
        else:
            if (a, coins) in lst:
                time[lst.index(elem)] += 1
            lst.append((a,) + coins)
            time.append(1)
            
            count_change_lst(a, coins[1:])
            count_change_lst(a - coins[0], coins)
    return count_change_lst
    
    #return sum(count_change(lst[i] * time[i]) for i in range(len(lst))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
