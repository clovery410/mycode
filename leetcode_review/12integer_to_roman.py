class Solution(object):
    def intToRoman(self, num):
        if num <= 0 or num >= 4000:
            return None
        res = ''
        s = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        weight = 1000
        for i in [6, 4, 2, 0]:
            d = (num / weight) % 10
            if d >= 1 and d <= 3:
                res += d * s[i]
            elif d == 4:
                res += s[i] + s[i+1]
            elif d == 5:
                res += s[i+1]
            elif d >= 6 and d <= 8:
                res += s[i+1] + (d-5) * s[i]
            elif d == 9:
                res += s[i] + s[i+2]
            weight /= 10
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.intToRoman(76)
