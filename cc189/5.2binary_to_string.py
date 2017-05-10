def printBinary(num):
    if num >= 1 or num < 0:
        return "Error"
    res = ["."]
    while num > 0:
        if len(res) > 32:
            return "Error"
        new_num = num * 2
        if new_num >= 1:
            res.append("1")
            num = new_num - 1
        else:
            res.append("0")
            num = new_num
    return ''.join(res)

if __name__ == "__main__":
    print printBinary(0.125)
