class Solution(object):
    def reverseWords(self, s):
        char_list = []
        start_idx = len(s) - 1
        
        while True:
            while start_idx >= 0 and s[start_idx] == ' ':
                start_idx -= 1
            if start_idx < 0:
                break
            end_idx = start_idx
            while start_idx >= 0 and s[start_idx] != ' ':
                start_idx -= 1
                
            char_list.append(s[start_idx+1: end_idx+1])
            
        return ' '.join(char_list)

if __name__ == "__main__":
    sol = Solution()
    s = "the sky, is blue"
    print sol.reverseWords(s)

            
        
