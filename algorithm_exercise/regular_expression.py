#solution1, recursive
def isMatch(string, regex):
    def checkNext(s_idx, r_idx):
        if s_idx >= len(string) and r_idx >= len(regex):
            return True
        if r_idx >= len(regex):
            return False

        cur_char = regex[r_idx]
        next_char = regex[r_idx+1] if r_idx + 1 < len(regex) else None
        if s_idx >= len(string):
            if next_char and next_char == '*' and checkNext(s_idx, r_idx+2):
                return True
            else: return False

        if next_char and next_char == '*':
            if (cur_char == string[s_idx] or cur_char == '.') and checkNext(s_idx+1, r_idx):
                return True
            else:
                return checkNext(s_idx, r_idx+2)
        else:
            if cur_char == string[s_idx] or cur_char == '.':
                return checkNext(s_idx+1, r_idx+1)
            else:
                return False

    return checkNext(0, 0)

if __name__ == "__main__":
    string = "aaaaaaaaaaaaab"
    regex = "a*a*a*a*a*a*a*a*a*a*c"
    print isMatch(string, regex)
