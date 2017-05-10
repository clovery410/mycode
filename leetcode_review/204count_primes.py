class Solution(object):
    # this solution will MLE, since hashmap consumes more memory than list to avoid collision
    def countPrimes(self, n):
        visited = set()
        count = 0
        for num in xrange(2, n):
            if num not in visited:
                count += 1
                start = num * num
                while start < n:
                    visited.add(start)
                    start += num
        return count

    #solution2, use list instead of set
    def countPrimes2(self, n):
        visited = [False for x in xrange(n+1)]
        count = 0
        for num in xrange(2, n):
            if visited[num] == False:
                count += 1
                start = num * num
                while start < n:
                    visited[start] = True
                    start += num
        return count

if __name__ == "__main__":
    sol = Solution()
    print sol.countPrimes(10)
