class Solution(object):
    def subsetsWithDup(self, nums):
        def helper(idx, cur_solution, all_solutions):
            if idx >= len(nums):
                all_solutions.add(tuple(cur_solution))
                return
            cur_solution.append(nums[idx])
            helper(idx+1, cur_solution, all_solutions)
            cur_solution.pop()
            helper(idx+1, cur_solution, all_solutions)

        nums.sort()
        res = set()
        helper(0, [], res)
        return list(list(elem) for elem in res)

    #solution2
    def subsetsWithDup2(self, nums):
        import collections
        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1
            
        def helper(items, item_idx, cur_sol):
            if item_idx == len(items):
                res.append(list(cur_sol))
                return

            num = items[item_idx][0]
            cnt = items[item_idx][1]

            for c in range(cnt + 1):
                for _ in range(c):
                    cur_sol.append(num)
                helper(items, item_idx+1, cur_sol)
                for _ in range(c):
                    cur_sol.pop()

        res = []
        helper(counts.items(), 0, [])
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.subsetsWithDup([4,4,4,1,4,1,4,1,4])
    print sol.subsetsWithDup2([4,4,4,1,4,1,4,1,4])

