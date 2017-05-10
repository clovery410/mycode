def regExp(s, t):
    def helper(idx_s, idx_t):
        if idx_s >= len(s) and idx_t >= len(t):
            return True
        if idx_s >= len(s) or idx_t >= len(t):
            return False
        if idx_t < len(t) - 1 and t[idx_t + 1] == '*':
            if helper(idx_s + 1, idx_t):
                return True
            elif helper(idx_s + 1, idx_t + 2):
                return True
            else:
                return False
        elif idx_t < len(t) - 1 and t[idx_t + 1] == '+':
            if s[idx_s] == t[idx_t] or t[idx_t] == '.':
                if helper(idx_s + 1, idx_t):
                    return True
                elif helper(idx_s + 1, idx_t + 2):
                    return True
                else:
                    return False
            else:
                return False
        elif (t[idx_t] == '.' or s[idx_s] == t[idx_t]) and helper(idx_s + 1, idx_t + 1):
            return True
        else:
            return False
    return helper(0, 0)

if __name__ == '__main__':
    s = 'aab'
    t = 'c*a*b+'
    print regExp(s, t)

