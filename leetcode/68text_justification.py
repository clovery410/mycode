class Solution(object):
    def fullJustify(self, words, maxWidth):
        length = []
        justify = []
        for word in words:
            length.append(len(word))

        curr_level = length[0]
        count = 1
        curr_remainder = maxWidth - curr_level - 1
        for i in xrange(len(length) - 1):
            next_l = length[i+1]
            if next_l < curr_remainder:
                curr_level += next_l + 1
                curr_remainder -= (1 + next_l)
                count += 1
            elif next_l == curr_remainder:
                justify.append([count+1, 0])
                curr_remainder = maxWidth
                curr_level = 0
                count = 0
            else:
                justify.append([count, curr_remainder+1])
                curr_remainder = maxWidth - next_l - 1
                curr_level = length[i]
                count = 1
        justify.append([count, 0])

        i = 0
        result = []
        for item in justify:
            if item[0] == 1:
                result.append(str(words[i]) + (maxWidth - len(words[i])) * " ")
                i += 1
            else:
                item_line = ""
                average_gap = item[1] / (item[0]-1) + 1
                extra_gap = item[1] % (item[0] - 1)
                for j in xrange(item[0]-1):
                    if extra_gap:
                        item_line += str(words[i]) + (average_gap + 1) * " "
                        extra_gap -= 1
                    else:
                        item_line += str(words[i]) + average_gap * " "
                    i += 1
                item_line += str(words[i])
                item_line += (maxWidth - len(item_line)) * " "
                i += 1
                result.append(item_line)

        print result


    def concise_version(self, words, maxWidth):
        result, curr, length_of_words = [], [], 0
        for word in words:
            if len(curr) + len(word) + length_of_words > maxWidth:
                if len(curr) == 1:
                    result.append(curr[0] + (maxWidth - length_of_words) * ' ')
                else:
                    total_space = maxWidth - length_of_words
                    average_space, extra_space = divmod(total_space, len(curr) - 1)
                    for i in xrange(extra_space):
                        curr[i] += ' '
                    result.append((average_space * ' ').join(curr))
                curr, length_of_words = [word], len(word)
            else:
                curr += [word]
                length_of_words += len(word)
        if curr:
            left_space = maxWidth - length_of_words - len(curr) + 1
            result.append(' '.join(curr) + left_space * ' ')
        return result                        


if __name__ == '__main__':
    words = ["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."]
    width = 8
    sol = Solution()
    sol.fullJustify(words, width)
    print sol.concise_version(words, width)
