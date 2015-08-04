def func_rec(a, b):
    if a == 0:
        return
    func_rec(a - 1, b)
    print(a * b)

result = func_rec(4, 7)
