def count_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return count_paths(m - 1, n) + count_paths(m, n - 1)

print(count_paths(3, 3))
