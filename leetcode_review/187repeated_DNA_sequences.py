class Solution(object):
    def findRepeatedDnaSequences(self, s):
        dna = collections.defaultdict(int)
        res = []
        for start_idx in xrange(len(s) - 9):
            key = s[start_idx: start_idx + 10]
            dna[key] += 1

        for key, value in dna.items():
            if value > 1:
                res.append(key)
        return res
            
