class Solution(object):
    def permutation(self, s):
        #get character counts
        from collections import defaultdict
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1

        #early break check here
        odd_count = sum(1 for x in counts.values() if x % 2 == 1)
        if odd_count > 1: return []

        def generate(counts):
            if all(value == 0 for value in counts.values()):
                return [['']]
            if sum(counts.values()) == 1:
                for key, val in counts.items():
                    if val == 1:
                        return [[key]]
            res = []
            for c in counts:
                if counts[c] >= 2:
                    counts[c] -= 2
                    for x in generate(counts):
                        res += [[c] + x + [c]]
                    # res += [[c] + x for x in generate(counts) + [c]]
                    counts[c] += 2
            return res
        return list(''.join(elem) for elem in generate(counts))

if __name__ == "__main__":
    sol = Solution()
    print sol.permutation('aabbc')
