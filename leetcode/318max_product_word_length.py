class Solution(object):
    def maxProduct(self, words):
        n = len(words)
        current_max = total_max = 0
        word_length = []
        word_pattern = [None for x in xrange(n)]
        for i in xrange(n):
            word_length.append(len(words[i]))
            s = set(words[i])
            if s in word_pattern:
                old = word_pattern.index(s)
                if word_length[old] < word_length[i]:
                    word_pattern[i] = s
                    word_pattern[old] = None
            else:
                word_pattern[i] = s

        print word_pattern
        for i in xrange(n):
            a = word_pattern[i]
            if a:
                for j in xrange(i+1, n):
                    b = word_pattern[j]
                    if b and a ^ b == a | b:
                        current_max = word_length[i] * word_length[j]
                        if current_max > total_max:
                            total_max = current_max

        return total_max


if __name__ == '__main__':
    words = ['a', 'ab', 'abc', 'ddccbbaa', 'cd', 'bcd', 'abcd']
    sol = Solution()
    print sol.maxProduct(words)
