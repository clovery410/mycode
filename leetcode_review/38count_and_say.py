class Solution(object):
    def countAndSay(self, n):
        cur_str = "1"
        for i in xrange(1, n):
            count = 1
            pre = cur_str[0]
            next_str = []
            for j in xrange(1, len(cur_str)):
                if cur_str[j] != pre:
                    next_str.append(str(count))
                    next_str.append(pre)
                    pre = cur_str[j]
                    count = 1
                else:
                    count += 1
            cur_str = ''.join(next_str) + str(count) + pre
        return cur_str

if __name__ == "__main__":
    sol = Solution()
    print sol.countAndSay(3)
