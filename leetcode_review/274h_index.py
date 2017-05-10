class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        res = 0
        for i in reversed(xrange(len(citations))):
            if citations[i] >= res + 1:
                res += 1
        return res

    #Solution2, use O(n) extra space can optimize running time to O(n)
    def hIndex2(self, citations):
        records = [0 for x in xrange(len(citations) + 1)]
        l = len(citations)
        cum = 0
        for citation in citations:
            if citation >= l:
                records[l] += 1
            else:
                records[citation] += 1
        
        for i in reversed(xrange(l+1)):
            cum += records[i]
            if cum >= i:
                return i
                
if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    sol = Solution()
    print sol.hIndex(citations)
    print sol.hIndex2(citations)
        
                
