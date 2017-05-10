class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        idx1 = idx2 = 0
        while idx1 < len(word) and idx2 < len(abbr):
            if abbr[idx2].isdigit():
                if abbr[idx2] == '0': return False
                end = idx2 + 1
                while end < len(abbr) and abbr[end].isdigit():
                    end += 1
                length = int(abbr[idx2:end])
                idx2 = end
                idx1 += length
            elif word[idx1] != abbr[idx2]:
                return False
            else:
                idx1 += 1
                idx2 += 1

        return True if idx1 == len(word) and idx2 == len(abbr) else False

if __name__ == "__main__":
    sol = Solution()
    word = "internationalization"
    abbr = "i12iz4n"
    print sol.validWordAbbreviation(word, abbr)
                
