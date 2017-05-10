class Solution(object):
    #solution1 uses extra space to split the string into an array
    def lengthOfLastWord(self, s):
        words = s.split(" ")
        return len(words[-1]) if len(words) > 0 else 0

    #solution2, if only use O(1) extra space, can go backward to check
    def lengthOfLastWord2(self, s):
        l = 0
        end = len(s) - 1
        while end >= 0 and s[end] == " ":
            end -= 1
        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        return end - start

if __name__ == "__main__":
    sol = Solution()
    s = "Hello World"
    print sol.lengthOfLastWord(s)
    print sol.lengthOfLastWord2(s)
