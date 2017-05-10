def reverseInteger(num):
    def helper(x):
        if x / 10 == 0:
            return (x, 1)
        next_num, next_weight = helper(x / 10)
        return (x % 10 * 10 ** next_weight + next_num, next_weight + 1)

    if num < 0:
        return -helper(-num)[0]
    return helper(num)[0]

print reverseInteger(-123)
