# Question: Leetcode 128 Longest Consecutive Sequence
# Given [100, 4, 200, 1, 3, 2], find the length of longest consecutive sequence,
# which is [1, 2, 3, 4] in this example, so return 4

# This is union find solution is implemented by array, which is learned from the java version

class UnionFind(object):
    def __init__(self, length):
        self.length = length
        self.identity = range(length)
        self.size = [1] * length

    def find(self, p):
        identity = self.identity
        while p != identity[p]:
            p = identity[identity[p]]
        return p

    def union(self, p, q):
        size = self.size
        identity = self.identity
        root_p = self.find(p)
        root_q = self.find(q)
        
        if root_p == root_q:
            return
        if size[root_p] < size[root_q]:
            identity[root_p] = root_q
            size[root_q] += size[root_p]
        else:
            identity[root_q] = root_p
            size[root_p] += size[root_q]

    def maxUnionSize(self):
        return max(self.size)

class Solution(object):
    def longestConsecutiveSequence(self, nums):
        res = 0
        uf = UnionFind(len(nums))
        visited = {}
        for i , num in enumerate(nums):
            if num in visited:
                continue
            visited[num] = i
            if visited.has_key(num-1):
                uf.union(i, visited[num-1])
            if visited.has_key(num+1):
                uf.union(i, visited[num+1])
                
        return uf.maxUnionSize()
