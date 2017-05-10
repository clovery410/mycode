class Solution(object):
    # Stupid solution...
    def intToRoman(self, num):
        roman = {}
        roman[1] = 'I'
        roman[5] = 'V'
        roman[10] = 'X'
        roman[50] = 'L'
        roman[100] = 'C'
        roman[500] = 'D'
        roman[1000] = 'M'
        
        def decode(num, ans):
            if num == 0:
                return
            elif num / 1000 > 0:
                ans.append(roman[1000])
                decode(num - 1000, ans)
            elif num / 500 > 0:
                if (num % 500) >= 400:
                    ans.append(roman[100])
                    ans.append(roman[1000])
                    decode(num - 900, ans)
                else:
                    ans.append(roman[500])
                    decode(num - 500, ans)
            elif num / 100 > 0:
                if (num / 100) == 4:
                    ans.append(roman[100])
                    ans.append(roman[500])
                    decode(num - 400, ans)
                else:
                    ans.append(roman[100])
                    decode(num - 100, ans)
            elif num / 50 > 0:
                if (num % 50) >= 40:
                    ans.append(roman[10])
                    ans.append(roman[100])
                    decode(num - 90, ans)
                else:
                    ans.append(roman[50])
                    decode(num - 50, ans)
            elif num / 10 > 0:
                if (num / 10) == 4:
                    ans.append(roman[10])
                    ans.append(roman[50])
                    decode(num - 40, ans)
                else:
                    ans.append(roman[10])
                    decode(num - 10, ans)
            elif num / 5 > 0:
                if (num % 5) >= 4:
                    ans.append(roman[1])
                    ans.append(roman[10])
                    decode(num - 9, ans)
                else:
                    ans.append(roman[5])
                    decode(num - 5, ans)
            elif num / 1 == 4:
                ans.append(roman[1])
                ans.append(roman[5])
                decode(num - 4, ans)
            else:
                ans.append(roman[1])
                decode(num - 1, ans)
                
        solution = []
        decode(num, solution)
        return ''.join(solution)

    # This solution is posted in the Leetcode Discuss, very clever and concise way, only need to consider the single, ten, hundred, and thousand digit
    def concise_version(self, num):
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        
        return M[num / 1000] + C[num % 1000 / 100] + X[num % 100 / 10] + I[num % 10]

    
