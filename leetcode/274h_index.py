class Solution(object):
    #Solution1, Binary search, Time O(nlogn), Space O(1)
    def hIndex(self, citations):
        citations.sort(reverse = True)
        s, e = 0, len(citations) - 1
        while s <= e:
            mid = (e - s) / 2 + s
            if citations[mid] == mid + 1:
                return mid + 1
            elif citations[mid] > mid + 1:
                s = mid + 1
            else:
                e = mid - 1
        return e + 1

    #Solution2, learnt from discuss, pretty smart, Time O(n), Space O(n)
    #Iterate the array for two rounds. In the first round we count how many citation in each bucket and int eh second round we traverse back to find maximum h.
    def hIndex2(self, citations):
        bucket = [0 for x in xrange(len(citations) + 1)]
        l = len(citations)
        for item in citations:
            index = min(item, l)
            bucket[index] += 1
        total = 0
        for i in reversed(xrange(len(bucket))):
            total += bucket[i]
            if total >= i:
                return i
        return 0

if __name__ == "__main__":
    sol = Solution()
    print sol.hIndex([0])
    print sol.hIndex2([3, 0, 6, 1, 5])
