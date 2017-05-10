def countInterpretation(s):
    def helper(s):
        if len(s) <= 1:
            return 1
        number = int(s[:2])
        count = 0
        if number <= 26:
            count += helper(s[2:])
        count += helper(s[1:])
        return count

    return helper(s)

print countInterpretation('11')
        
