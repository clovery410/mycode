class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0: return "NaN"
        if numerator == 0: return "0"
        
        res = []
        neg = (numerator < 0) != (denominator < 0)
        if neg:
            res.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        res.append(str(numerator / denominator))
        
        fraction = numerator % denominator
        if fraction > 0:
            res.append(".")
            fraction_str = []
            used = {}
            while fraction > 0:
                if fraction in used:
                    idx = used[fraction]
                    res.extend(fraction_str[:idx] + ["("] + fraction_str[idx:] + [")"])
                    return ''.join(res)
                used[fraction] = len(fraction_str)
                fraction *= 10
                fraction_str.append(str(fraction / denominator))
                fraction %= denominator
            res.extend(fraction_str)
            
        return ''.join(res)

if __name__ == "__main__":
    sol = Solution()
    print sol.fractionToDecimal(1, 21)
            
        
