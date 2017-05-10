class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        res = []
        s, e = 0, len(nums) - 1
        needReverse = True if a >= 0 else False
        while s <= e:
            num1, num2 = nums[s], nums[e]
            res1 = a * num1 ** 2 + b * num1 + c
            res2 = a * num2 ** 2 + b * num2 + c
            if res1 == res2:
                res.append(res1)
                s += 1
            elif res1 < res2:
                if needReverse:
                    res.append(res2)
                    e -= 1
                else:
                    res.append(res1)
                    s += 1
            else:
                if needReverse:
                    res.append(res1)
                    s += 1
                else:
                    res.append(res2)
                    e -= 1
        return res[::-1] if needReverse else res

if __name__ == "__main__":
    sol = Solution()
    nums = [-4, -2, 2, 4]
    print sol.sortTransformedArray(nums, -1, 3, 5)
                    
