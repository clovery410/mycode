class Solution(object):
    #wrong solution.....
    def candy(self, ratings):
        res = len(ratings)
        if res == 0: return 0

        up_count, down_count = 1, 1
        for i in xrange(1, len(ratings)):
            print res, up_count, down_count
            cur, pre = ratings[i], ratings[i-1]
            if cur > pre:
                if down_count > 1:
                    res += (1 + down_count-1) * (down_count-1) / 2
                down_count = 1
                up_count += 1
            elif cur < pre:
                if up_count > 1:
                    res += (1 + up_count-1) * (up_count-1) / 2
                up_count = 1
                down_count += 1
            else:
                up_count, down_count = 1, 1

        print res
        print up_count, down_count
        if up_count > 1:
            res += (1 + up_count-1) * (up_count-1) / 2
        if down_count > 1:
            res += (1 + down_count-1) * (down_count-1) / 2
        return res

    #solution2
    def candy2(self, ratings):
        res = [1] * len(ratings)
        if len(res) == 0: return 0

        #scan forward
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        #scan backward
        for i in reversed(xrange(len(ratings)-1)):
            if ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                res[i] = res[i+1] + 1

        return sum(res)

if __name__ == "__main__":
    ratings = [1,3,2,1,2,4,1,3]
    sol = Solution()
    print sol.candy(ratings)
    print sol.candy2(ratings)
