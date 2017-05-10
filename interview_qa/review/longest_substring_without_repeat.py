def longestSubstring(s):
    max_len = 0
    cur_start = 0
    visited = {}
    res_idx = []
    for i, c in enumerate(s):
        if c in visited:
            cur_start = visited[c] + 1
            visited[c] = i
            if i - cur_start + 1 > max_len:
                res_idx = (cur_start, i)
                max_len = i - cur_start + 1
        else:
            visited[c] = i

    if i - cur_start + 1 > max_len:
        res_idx = (cur_start, i)

    return s[res_idx[0]: res_idx[1]+1]

#print longestSubstring("abcdabes")
print longestSubstring("abcdbef")

