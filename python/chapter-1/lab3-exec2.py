def hailstone(n):
    if n == 1:
        return 1 
    elif n % 2 == 0:
        print(n / 2)
        return 1 + hailstone(n / 2)
    else:
        print(n * 3 + 1)
        return 1 + hailstone(n * 3 + 1)


result = hailstone(9)
print(result)

#The Answer
def hailstone1(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone1(n / 2)
    else:
        return 1 + hailstone1(n * 3 + 1)
