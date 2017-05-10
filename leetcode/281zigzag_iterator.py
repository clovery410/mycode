class ZigzagIterator(object):
    def __init__(self, nums1, nums2):
        self.nums1= nums1
        self.nums2 = nums2
        self.idx1 = 0
        self.idx2 = 0
        self.turn = 1
        
    def hasNext(self):
        if self.idx1 >= len(self.nums1) and self.idx2 >= len(self.nums2):
            return False
        if self.turn == 1 and self.idx1 >= len(self.nums1):
            self.turn = 2
        if self.turn == 2 and self.idx2 >= len(self.nums2):
            self.turn = 1
        return True

    def next(self):
        if self.turn == 1:
            res = self.nums1[self.idx1]
            self.idx1 += 1
            self.turn = 2
        else:
            res = self.nums2[self.idx2]
            self.idx2 += 1
            self.turn = 1
        return res

if __name__ == "__main__":
    nums1= [1,2,3,4]
    nums2 = [6,7]
    zi = ZigzagIterator(nums1, nums2)
    while zi.hasNext():
        print zi.next()
