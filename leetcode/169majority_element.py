class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        count = {}
        for item in nums:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1

            if count[item] > n / 2:
                return item

    def moore_majority_vote(self, nums):
        # Step1 if the counter is 0, set the current candidate to x and the counter to 1, if the counter is not 0, increment or decrement the counter based on whether x is the current candidate.
        count = 0
        for item in nums:
            if count == 0:
                candidate = item
                count = 1
            elif candidate == item:
                count += 1
            else:
                count -= 1

        # Step2 Check whether majority exists
        count = 0
        n = len(nums)
        for item in nums:
            if item == candidate:
                count += 1
        if count > n / 2:
            return candidate
        else:
            return None

if __name__ == '__main__':
    nums = [1, 2, 2, 2]
    sol = Solution()
    print sol.majorityElement(nums)
                    
