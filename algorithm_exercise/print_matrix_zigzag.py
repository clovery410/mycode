def printZigzag(matrix):
    m, n = len(matrix), len(matrix[0]) if len(matrix) else 0
    if m == 0 or n == 0:
        return

    _sum = m + n
    for k in xrange(_sum+1):
        if k % 2 == 0:
            start = 0 if k <= n else k - n + 1
            end = k+1 if k < m else m
            for i in xrange(start, end):
                j = k - i
                print matrix[i][j]
        else:
            start = 0 if k <= m else k - m + 1
            end = k+1 if k < n else n
            for j in xrange(start, end):
                i = k - j
                print matrix[i][j]

if __name__ == "__main__":
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
    printZigzag(matrix)
