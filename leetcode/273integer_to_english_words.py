class Solution(object):
    def numberToWords(self, num):
        def generateWord(num, weight):
            if num <= 0:
                return []
            single = num % 10
            tens = (num / 10) % 10
            hundred = (num / 100) % 10
            cur_res = []
            if hundred > 0:
                cur_res.append(digit1[hundred])
                cur_res.append("Hundred")
            if tens == 1:
                cur_res.append(digit2[tens * 10 + single])
            else:
                if tens > 1:
                    cur_res.append(digit3[tens])
                if single > 0:
                    cur_res.append(digit1[single])
                    
            if num % 1000 > 0 and weight > 0:
                cur_res.append(posfix[weight])
            return generateWord(num / 1000, weight + 1) + cur_res

        digit1 = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        digit2 = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        digit3 = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
        posfix = {1: "Thousand ", 2: "Million ", 3: "Billion "}

        if num == 0:
            return "Zero"
        return ' '.join(generateWord(num, 0))

if __name__ == "__main__":
    sol = Solution()
    print sol.numberToWords(1234567)
