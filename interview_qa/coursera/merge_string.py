def mergeString(s1, s2):
    l1, l2 = len(s1), len(s2)
    if l1 > l2: return mergeString(s1[:l2], s2+s1[l2:])

    temp = [''] * 2 * l1
    for i in range(l1):
        temp[i*2] = s1[i]
        temp[i*2+1] = s2[i]

    return ''.join(temp) + s2[l1:l2]

if __name__ == "__main__":
    print mergeString("defhgi", "abc")
