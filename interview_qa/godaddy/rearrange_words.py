def  rearrangeWord(word):
    def reverseString(start_idx, end_idx):
        while start_idx < end_idx:
            chars[start_idx], chars[end_idx] = chars[end_idx], chars[start_idx]
            start_idx += 1
            end_idx -= 1
    
    chars = list(word)
    n = len(chars)
    i = n - 2
    while i >= 0 and chars[i] >= chars[i+1]:
        i -= 1
        
    if i < 0:
        return "no answer"
    
    j = n - 1
    while j > i:
        if chars[j] > chars[i]:
            chars[j], chars[i] = chars[i], chars[j]
            break
        j -= 1
        
    reverseString(i + 1, n - 1)
    return ''.join(chars)
