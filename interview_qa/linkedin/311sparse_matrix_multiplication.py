import collections
class Solution(object):
    # pre-store non zero indices of matrix A
    def multiply(self, A, B):
        m1, n1 = len(A), len(A[0]) if len(A) else 0
        m2, n2 = len(A), len(B[0]) if len(B) else 0
        C = [[0 for x in xrange(n2)] for x in xrange(m1)]

        non_zero_A = collections.defaultdict(list)
        for i in xrange(m1):
            for j in xrange(n1):
                if A[i][j] != 0:
                    non_zero_A[i].append(j)

        for idx, vals in non_zero_A.items():
            for j in xrange(n2):
                cur_res = 0
                for jj in vals:
                    cur_res += A[idx][jj] * B[jj][j]
                C[idx][j] = cur_res
                
        return C

if __name__ == "__main__":
    sol = Solution()
    A = [[1,-5]]
    B = [[12],[-1]]
    print sol.multiply(A, B)
