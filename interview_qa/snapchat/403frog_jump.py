import collections
class Solution(object):
    def canCross(self, stones):
        if stones[1] != 1:
            return False
        dp = collections.defaultdict(set)
        dp[1] = {1}
        dest_stone = stones[-1]

        for i in xrange(1, len(stones)):
            stone_num = stones[i]
            for step in dp[stone_num]:
                for k in xrange(max(1, step-1), step+2):
                    if stone_num + k == dest_stone:
                        return True
                    dp[stone_num+k].add(k)

        return len(dp[dest_stone]) > 0

    # solution2, re-write updating dp part, since we do not need to update the stones that is not in stones list, so initialization part should make some change
    def canCross2(self, stones):
        if stones[1] != 1:
            return False
        dp = {x : set() for x in stones}
        dp[1].add(1)
        dest_stone = stones[-1]

        for i in xrange(1, len(stones)):
            stone = stones[i]
            for step in dp[stone]:
                for new_step in [step - 1, step, step + 1]:
                    if new_step > 0 and stone + new_step in dp:
                        if stone + new_step == dest_stone:
                            return True
                        dp[stone+new_step].add(new_step)

        return len(dp[dest_stone]) > 0

    # solution3, intuitive recursive solution
    def canCross3(self, stones):
        def check(stone, step):
            if stone == dest:
                return True
            if (stone, step) in failed:
                return False
            
            for new_step in [step - 1, step, step + 1]:
                if new_step > 0 and stone + new_step in stones and check(stone+new_step, new_step):
                    return True

            failed.add((stone, step))
            return False
        
        dest = stones[-1]
        stones = set(stones)
        failed = set()
        return check(0, 0)
                

if __name__ == "__main__":
    sol = Solution()
    stones = [0,1,2,3,4,8,9,11]
    stones2 = [0,1,3,5,6,8,12,17]
    print sol.canCross(stones2)
    print sol.canCross2(stones2)
    print sol.canCross3(stones2)
