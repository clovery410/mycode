def  missingWords(s, t):
    s_chars = s.split(" ")
    t_chars = t.split(" ")
    res = []
    s_i, t_i = 0, 0
    while s_i < len(s_chars) and t_i < len(t_chars):
        if s_chars[s_i] != t_chars[t_i]:
            res.append(s_chars[s_i])
        else:            
            t_i += 1
        s_i += 1
        
    while s_i < len(s_chars):
        res.append(s_chars[s_i])
        s_i += 1
        
    return res
