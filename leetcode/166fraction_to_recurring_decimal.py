class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return "NaN"
        res = ""
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            res += "-"
            numerator = abs(numerator)
            denominator = abs(denominator)
            
        quotient = numerator / denominator
        remainder = numerator - quotient * denominator
        res += str(quotient)
        if remainder != 0:
            res += "."
            cache = {}
            fraction = ""
            index = 0
            while remainder != 0:
                quotient = remainder * 10 / denominator
                remainder = remainder * 10 - quotient * denominator
                if (quotient, remainder) in cache:
                    return res + fraction[:cache[(quotient, remainder)]] + "(" + fraction[cache[(quotient, remainder)]:] + ")"
                elif (quotient, remainder) not in cache:
                    cache[(quotient, remainder)] = index
                    index += 1
                fraction += str(quotient)
            return res + fraction
        return res


if __name__ == "__main__":
    sol = Solution()
    print sol.fractionToDecimal(1, 12)
            
        
