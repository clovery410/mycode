cache = {}

def dp_alignment(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    max_comment = 0
    if (s1, s2) in cache:
        return cache[(s1, s2)]
    if s1[0] == s2[0]:
        max_comment = dp_alignment(s1[1:], s2[1:]) + 1
        cache[(s1, s2)] = max_comment
        return max_comment
    else:
        max_comment = max(dp_alignment(s1, s2[1:]), dp_alignment(s1[1:], s2))
        cache[(s1, s2)] = max_comment
        return max_comment
                

if __name__ == '__main__':
    string1 = 'nematode knowledge'
    string2 = 'empty bottle'

    comment = dp_alignment(string1, string2)

    print(cache)
    print(comment)

    # count = 0
    # for element in cache:
    #     if cache[element] > count:
    #         count = cache[element]
    #         max_subsequence = element
    # print(max_subsequence)
