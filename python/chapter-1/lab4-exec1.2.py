def gcb_recur(a, b):
    smaller_para = min(a, b)
    larger_para = max(a, b)
    remainder = larger_para % smaller_para
    if smaller_para % remainder == 0:
        return remainder
    return gcb_recur(smaller_para, remainder)

print(gcb_recur(50, 35))


def gcb_itera(a, b):
    smaller_para = min(a, b)
    larger_para = max(a, b)
    remainder = larger_para % smaller_para
    while not smaller_para % remainder == 0:
        smaller_para, remainder = remainder, smaller_para % remainder
    return remainder

print(gcb_itera(50, 35))
