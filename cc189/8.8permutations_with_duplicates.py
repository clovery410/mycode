from collections import defaultdict
class Solution(object):
    def permutations(self, unique):
        def helper(s):
            if all(value == 0 for value in unique.values()):
                return ['']
            cur = []
            for key in unique:
                if unique[key] > 0:
                    unique[key] -= 1
                    cur.extend([c + key for c in helper(unique)])
                    unique[key] += 1
            return cur
        
        unique = defaultdict(int)
        for c in s:
            unique[c] += 1
        return helper(unique)

if __name__ == "__main__":
    s = "aabbbbc"
    sol = Solution()
    print len(sol.permutations(s))
        
            
