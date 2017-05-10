class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = collections.defaultdict(int)
        for letter in magazine:
            count[letter] += 1
        for letter in ransomNote:
            if count[letter] <= 0:
                return False
            count[letter] -= 1
        return True
