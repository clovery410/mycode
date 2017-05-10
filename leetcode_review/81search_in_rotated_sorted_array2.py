# 1, 1, 1, 1, 2, 3, 1
# 5, 6, 1, 2, 3, 4
class Solution(object):
    def search(self, nums, target):
        s, e = 0, len(nums) - 1
        while s <= e:
            mid = (e - s) / 2 + s
            if nums[mid] == target:
                return True
            if nums[s] == nums[e] == nums[mid]:
                while s <= mid and nums[s] == nums[mid]:
                    s += 1
                while e >= mid and nums[e] == nums[mid]:
                    e -= 1
            elif nums[s] > target and nums[mid] > nums[e]:
                s = mid + 1
            elif nums[e] < target and nums[mid] < nums[s]:
                e = mid - 1
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return False

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 2, 3, 1]
    print sol.search(nums, 4)
