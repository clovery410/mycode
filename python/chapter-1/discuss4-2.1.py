# 2.1 I want to go up a flight of stairs that has n steps. I can either take 1 or 2 steps each time. How many different ways can I go up this flight of stairs? Write a function count_stairs_ways that solves this problem for me.
def count_stairs_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stairs_ways(n - 1) + count_stairs_ways(n - 2)
