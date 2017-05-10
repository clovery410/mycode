class Solution(object):
    def hIndex(self, citations):
        l = len(citations)
        s, e = 0, l - 1
        while s <= e:
            mid = (e - s) / 2 + s
            if citations[mid] >= l - mid :
                e = mid - 1
            else:
                s = mid + 1
        return l - s

if __name__ == "__main__":
    citations = [1,2,3,4]
    sol = Solution()
    print sol.hIndex(citations)
