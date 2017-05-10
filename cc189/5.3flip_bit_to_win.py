#assume the integer is 4 bytes, which is 32 bits
def longestSequence(num):
    if num == -1:
        return 32
    #get the two's complement binary representation
    if num >= 0:
        binary = format(num, '032b')
    else:
        binary = format((1 << 32) + num, '032b')
    sequence = getSequence(binary)
    max_len = 1
    for i in range(0, len(sequence), 2):
        if sequence[i] == 1:
            leftCount = sequence[i-1] if i > 0 else 0
            rightCount = sequence[i+1] if i < len(sequence) - 1 else 0
            max_len = max(max_len, leftCount + rightCount + 1)
    return max_len

def getSequence(binary):
    res = []
    count = 0
    searchFor = 0
    for i in range(32):
        if int(binary[i]) != searchFor:
            res.append(count)
            count = 1
            searchFor ^= 1
        else:
            count += 1
    res.append(count)
    return res

#solution2, try to reduce the space complexcity
def flipBit(num):
    if ~num == 0:
        return 32
    preLength, curLength = 0, 0
    maxLength = 1
    for i in range(32):
        if (num & 1) == 1:
            curLength += 1
        else:
            # here, if we are at the last bit or the next bit is 0, then should we set preLength to 0
            if i == 31 or num & 2 == 0: 
                preLength = 0
            else:
                preLength = curLength
            curLength = 0
        maxLength = max(maxLength, curLength + preLength + 1)
        num >>= 1
    return maxLength

if __name__ == "__main__":
    print longestSequence(1775)
    print flipBit(1775)
    
    
