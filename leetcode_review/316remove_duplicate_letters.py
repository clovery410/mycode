import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        counts = collections.defaultdict(int)
        distinct_s = set()
        
        for c in s:
            counts[c] += 1
        stack = []
        for c in s:
            if c not in distinct_s:
                while len(stack) > 0 and c < stack[-1] and counts[stack[-1]] > 1:
                    rm_c = stack.pop()
                    counts[rm_c] -= 1
                    distinct_s.remove(rm_c)
                stack.append(c)
                distinct_s.add(c)
            else:
                counts[c] -= 1
        return ''.join(stack)

if __name__ == "__main__":
    sol = Solution()
    string = "cbacdcbc"
    s = "abacb"
    s2 = "bbcaac"
    print sol.removeDuplicateLetters(s2)
                
