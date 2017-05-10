#solution1, each time manipulate a single bit
def insertion(m, n, i, j):
    idx = 0
    while m != 0:
        mask = ~(1 << (i + idx))
        n = (n & mask) | ((m & 1) << (i + idx))
        m = m >> 1
        idx += 1
    return n

#solution2, tackle all bits at the same time
def insertion2(m, n, i, j):
    #first, create a mask to clear bits i through bits j in n. which means the mask should look like from bit i to bit j are all 0s, other bits are all 1s
    allOnes = ~0
    leftOnes = allOnes << (j+1)
    rightOnes = (1 << i) - 1
    mask = leftOnes | rightOnes

    #then, clear bits j through i, and put m in there
    n_cleared = n & mask  # clear bits j through i
    m_shifted = m << i  # move m into correct position
    return n_cleared | m_shifted

if __name__ == "__main__":
    print bin(insertion(19, pow(2, 10), 2, 6))
    print bin(insertion2(19, pow(2, 10), 2, 6))
