class Solution(object):
    def numberOfPatterns(self, m, n):
        def generate(count, idx):
            if mark[idx]: return

            count += 1
            if count > n:
                return
            if m <= count <= n:
                self.total_count += 1

            mark[idx] = True
            for j in range(1, 10):
                if j != idx:
                    if (idx, j) in across:
                        if mark[across[(idx, j)]]: generate(count, j)
                    else:
                        generate(count, j)
            mark[idx] = False

        mark = [False] * 10
        across = {(1, 3): 2, (4, 6): 5, (7, 9): 8, (1, 7): 4, (2, 8): 5, (3, 9): 6, (3, 7): 5, (1, 9): 5,
                  (3, 1): 2, (6, 4): 5, (9, 7): 8, (7, 1): 4, (8, 2): 5, (9, 3): 6, (7, 3): 5, (9, 1): 5}
        
        self.total_count = 0
        for i in range(1, 10):
            generate(0, i)
        return self.total_count

if __name__ == "__main__":
    sol = Solution()
    print sol.numberOfPatterns(2, 3)
