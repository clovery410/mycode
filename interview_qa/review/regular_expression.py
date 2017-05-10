def regular_expression(string, regex):
    def checkNext(s_i, r_i):
        if s_i >= len(string) and r_i >= len(regex):
            return True
        if r_i >= len(regex):
            return False

        cur_char = regex[r_i]
        next_char = regex[r_i + 1] if r_i + 1 < len(regex) else None
        if next_char and next_char == '*':
            # match zero
            if checkNext(s_i, r_i+2):
                return True
            # match one or more
            if (cur_char == string[s_i] or cur_char == '.') and checkNext(s_i+1, r_i):
                return True

        elif cur_char == string[s_i] or cur_char == '.':
            return checkNext(s_i + 1, r_i + 1)

        return False

    return checkNext(0, 0)

print regular_expression("abcd", "ad*b*.d")
                

