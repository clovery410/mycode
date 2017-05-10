def getSortedList():
    n = int(raw_input("Enter length of name list:"))
    names = []
    for i in range(n):
        names.append(raw_input("enter name:").split(" "))
    names.sort(key = lambda x: (x[0], getValue(x[1])))
    return [" ".join(x) for x in names]

def getValue(ordinal):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50}
    l = len(ordinal)
    if l == 0: return 0
    num = roman[ordinal[-1]]
    for i in reversed(range(l-1)):
        cur, _next = roman[ordinal[i]], roman[ordinal[i+1]]
        if cur >= _next:
            num += cur
        else:
            num -= cur
    return num

if __name__ == "__main__":
    print getSortedList()
