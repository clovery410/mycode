class NumArray(object):
    def __init__(self, nums):
        self.sums = [0] + nums[:]
        for i in range(1, len(self.sums)):
            self.sums[i] += self.sums[i-1]

    def sumRange(self, i, j):
        return self.sums[j+1] - self.sums[i]

if __name__ =="__main__":
    num = NumArray([1,-1,2,-3])
    print num.sumRange(0, 3)
        
