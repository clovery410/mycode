def buildSubsequence(s):
    def generate(idx, cur_sol, all_sols):
        if idx >= len(s):
            if len(cur_sol) > 0:
                all_sols.add(tuple(cur_sol))
            return
        generate(idx+1, cur_sol, all_sols)
        cur_sol.append(s[idx])
        generate(idx+1, cur_sol, all_sols)
        cur_sol.pop()

    res = set()
    generate(0, [], res)
    return sorted([''.join(elem) for elem in res])

# solution2, use bisect to enforce order
def buildSubsequence2(s):
    import bisect
    def generate(idx, cur_sol, all_sols):
        if idx >= len(s):
            if len(cur_sol) > 0:
                bisect.insort_left(all_sols, list(cur_sol))
            return
        generate(idx+1, cur_sol, all_sols)
        cur_sol.append(s[idx])
        generate(idx+1, cur_sol, all_sols)
        cur_sol.pop()

    res = []
    generate(0, [], res)
    return [''.join(elem) for elem in res]
        

if __name__ == "__main__":
    s = "abc"
    print buildSubsequence(s)
    print buildSubsequence2(s)
        
