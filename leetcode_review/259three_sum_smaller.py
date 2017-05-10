class Solution(object):
    #solution1, if only need to return the combination count, implemented as bellow:
    def threeSumSmaller(self, nums, target):
        res = 0
        nums.sort()

        for i in xrange(len(nums)-2):
            first = nums[i]
            s, e = i + 1, len(nums) - 1
            while s < e:
                if first + nums[s] + nums[e] < target:
                    res += e - s
                    s += 1
                else:
                    e -= 1
        return res
    
    #solution2, if need to return all combination of index triplets, implemented as bellow:
    def threeSumSmaller2(self, nums, target):
        res = []
        new_nums = [(num, i) for i, num in enumerate(nums)]
        new_nums.sort()

        for i in xrange(len(new_nums)-2):
            first, idx1 = new_nums[i]
            s, e = i + 1, len(new_nums) - 1
            while s < e:
                second, idx2 = new_nums[s]
                third, idx3 = new_nums[e]
                if first + second + third < target:
                    for k in xrange(s+1, e+1):
                        k_val, k_idx = new_nums[k]
                        indices = sorted([idx1, idx2, k_idx])
                        res.append(indices)
                    s += 1
                else:
                    e -= 1
        return res

    

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,2]
    target = 50
    print sol.threeSumSmaller(nums, target)
    print sol.threeSumSmaller2(nums, target)
            
