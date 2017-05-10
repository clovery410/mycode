class Solution(object):
    def isAdditiveNumber(self, num):
        def check(pre_num, cur_num, start_idx):
            if start_idx >= len(num):
                return True
            next_num = str(int(pre_num) + int(cur_num))
            end_idx = start_idx + len(next_num)
            if num[start_idx:end_idx] == next_num and check(cur_num, next_num, end_idx):
                return True
            else:
                return False

        if len(num) < 3:
            return False
        for i in xrange(1, len(num)-1):
            for j in xrange(i+1, len(num)):
                if (i == 1 or num[0] != '0') and (j == i+1 or num[i] != '0') and check(num[:i], num[i:j], j):
                    print num[:i], num[i:j]
                    return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print sol.isAdditiveNumber("1023")
