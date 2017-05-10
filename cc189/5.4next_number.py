def getNext(num):
    #find the rightmost non-trailing zero, flip it to 1
    zero_idx = -1
    count = 0
    searchFor = 1
    zero_count = 0
    while count < 2:
        zero_idx += 1
        if zero_idx == 32:
            return -1
        if num & (1 << zero_idx) == 0:
            zero_count += 1
        if (num & (1 << zero_idx)) >> zero_idx == searchFor:
            searchFor ^= 1
            count += 1

    #flip the rightmost non-trailing zero to 1
    num |= (1 << zero_idx)

    #clear all the bit on the right side
    num &= (-1 << zero_idx)

    #insert remaining 1s on the right most side
    one_count = zero_idx - zero_count
    num |= ((1 << one_count) - 1)

    return num

def getPrev(num):
    #find the rightmost non-trailing one, and flip it to 0
    one_idx = -1
    count = 0
    searchFor = 0
    one_count = 0
    while count < 2:
        one_idx += 1
        if one_idx == 32:
            return -1
        if (num & (1 << one_idx)) >> one_idx == 1:
            one_count += 1
        if (num & (1 << one_idx)) >> one_idx == searchFor:
            searchFor ^= 1
            count += 1

    #flip the rightmost non-trailing one to 0
    num &= ((~0) << one_idx+1)

    #create the mask, with calculated counts of 1s on the right, then shift these 1s to the left
    zero_count = one_idx - one_count
    mask = (1 << one_count) - 1
    num |= (mask << zero_count)

    return num
    
if __name__ == "__main__":
    print getNext(131)
    print getPrev(131)
