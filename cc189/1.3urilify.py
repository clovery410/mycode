"""
Questions: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.(Note: if implementing in Java, please use a character array so that you can perform this operation in place.)
"""
#idea: first calculate the valid spaces in the string, then we can know the total length we need. Initialize a total length of array, fill the array backward.
def urlify(s, length):
    spaceCount = 0
    for i in range(length):
        if s[i] == ' ':
            spaceCount += 1

    totalLength = length + spaceCount * 2
    j = totalLength - 1
    res = [None] * totalLength
    for i in reversed(range(length)):
        if s[i] == ' ':
            res[j] = '0'
            res[j-1] = '2'
            res[j-2] = '%'
            j -= 3
        else:
            res[j] = s[i]
            j -= 1
    return ''.join(res)

if __name__ == "__main__":
    print urlify("Mr John Smith         ", 13)
