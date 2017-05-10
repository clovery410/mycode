class Solution(object):
    def canCross(self, stones):
        def dfs(idx, k):
            if (idx, k) in memo:
                return False
            if idx == len(stones) - 1:
                return True
            for i in xrange(idx+1, len(stones)):
                gap = stones[i] - stones[idx]
                if gap < k - 1:
                    continue
                elif gap > k + 1:
                    memo.add((idx, gap))
                    return False
                elif dfs(i, gap):
                    return True
            memo.add((idx, k))
            return False
        memo = set()
        return len(stones) < 2 or stones[1] - stones[0] <= 1 and dfs(1, 1)

    #solution2, dp solution
    def canCross2(self, stones):
        if stones[1] != 1:
            return False
        
        dp = {x: set() for x in stones}
        dp[1].add(1)
        
        for stone in stones[:-1]:
            for step in dp[stone]:
                for new_step in [step-1, step, step+1]:
                    if new_step > 0 and stone + new_step in dp:
                        dp[stone + new_step].add(new_step)
                        
        return bool(dp[stones[-1]])

if __name__ == "__main__":
    sol = Solution()
    stones = [0,1,3,5,6,8,12,17]
    stones2 = [0,1,2,3,4,8,9,11]
    stones3 = [0,2]
    print sol.canCross2(stones)
                
                
