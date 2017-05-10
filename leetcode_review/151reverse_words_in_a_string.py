class Solution(object):
    def reverseWords(self, s):
        char_list = []
        start_idx = 0
        while True:
            while start_idx < len(s) and s[start_idx] == " ":
                start_idx += 1

            if start_idx >= len(s):
                break

            end_idx = start_idx
            while end_idx < len(s) and s[end_idx] != " ":
                end_idx += 1
            char_list.append(s[start_idx: end_idx])
            start_idx = end_idx

        return ' '.join(x for x in reversed(char_list))

if __name__ == "__main__":
    sol = Solution()
    print sol.reverseWords("Hello,  World!")
