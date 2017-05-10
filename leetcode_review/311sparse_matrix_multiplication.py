class Solution(object):
    def multiply(self, A, B):
        import collections
        m1, n1 = len(A), len(A[0]) if len(A) > 0 else 0
        m2, n2 = len(B), len(B[0]) if len(B) > 0 else 0
        
        col_map = collections.defaultdict(list)
        for j in xrange(n2):
            for i in xrange(m2):
                if B[i][j] != 0:
                    col_map[j].append((i, B[i][j]))

        res = [[0 for x in xrange(n2)] for x in xrange(m1)]
        for i in xrange(m1):
            for j in xrange(n2):
                cur_val = 0
                for idx, col_val in col_map[j]:
                    cur_val += A[i][idx] * col_val
                res[i][j] = cur_val
        return res

