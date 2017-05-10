import sys
def crossRiver(A, D):
    if D > len(A): return 0

    #initial
    dp = [0] * (len(A) + 1)
    for i in xrange(D):
        dp[i] = A[i]

    for i in xrange(D, len(A)):
        if A[i] == -1:
            dp[i] == -1
        else:
            count = 0
            temp = sys.maxint
            for j in xrange(1, D+1):
                if dp[i-j] == -1:
                    count += 1
                else:
                    temp = min(temp, dp[i-j])
            dp[i] = max(temp, A[i])
    res = sys.maxint
    count = 0
    for j in xrange(1, D+1):
        if dp[len(A) - j] == -1:
            count += 1
        else:
            res = min(res, dp[len(A)-j])
    print dp
    return -1 if count == D else res

if __name__ == "__main__":
    A = [1,-1,0,2,3,5]
    D = 3
    print crossRiver(A, D)
            
