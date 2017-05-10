class Solution(object):
    # sort first, so running time is O(n logn), space is O(1)
    def hIndex(self, citations):
        citations.sort(reverse = True)

        for i, citation in enumerate(citations):
            if citation < i + 1:
                return i
        return i + 1

    # if can use extra space, can do it in linear time
    def hIndex2(self, citations):
        records = [0] * (len(citations) + 1)
        for citation in citations:
            if citation > len(citations):
                records[-1] += 1
            else:
                records[citation] += 1
                
        res = 0
        for i in reversed(xrange(len(records))):
            res += records[i]
            if res >= i:
                return i

if __name__ == "__main__":
    sol = Solution()
    citations = [3, 0, 6, 1, 5]
    print sol.hIndex(citations)
