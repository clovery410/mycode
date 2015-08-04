def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game if we start with n disks on the start pole and want to move them all to the end pole.

    The game is to assumed to have 3 poles (which is traditional).

    >>> towers_of_hanoi(1, 1, 3)
    Move 1 disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move 1 disk from rod 1 to rod 2
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 1 to rod 2
    Move 1 disk from rod 3 to rod 2
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 2 to rod 1
    Move 1 disk from rod 2 to rod 3
    Move 1 disk from rod 1 to rod 3
    """
    trans = 6 - start - end
    if n == 1:
        move_disk(start, end)
    else:
        towers_of_hanoi(n - 1, start, trans)
        move_disk(start, end)
        towers_of_hanoi(n - 1, trans, end)
        

def move_disk(start, end):
    print("Move 1 disk from rod", start, "to rod", end)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

result = towers_of_hanoi(4, 1, 3)
