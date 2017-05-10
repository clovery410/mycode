celebrity = [[1,1,0], [0,1,1], [0,1,1]]
def knows(a, b):
    return celebrity[a][b]

class Solution(object):
    #solution1, TLE... and too verbose
    def findCelebrity(self, n):
        count = [0] * n
        knowOther = [False] * n
        candidates = []
        k = 0
        for i in xrange(1, n):
            if knows(0, i):
                k += 1
                count[i] = 1
                candidates.append(i)
            if knows(i, 0):
                knowOther[i] = True

        # if k == 0, this means 0 does not know anyone, then we need check whether everyone knows 0
        if k == 0:
            for j in xrange(1, n):
                if not knows(j, 0):
                    return -1
                knowOther[j] = True
            return 0

        print count
        # else, 0 is not celebrity, find celebrity from candidate of whom 0 knows
        for i in xrange(1, n):
            new_candidates = [i]
            print candidates
            for j in candidates:
                if i != j and knows(i, j):
                    knowOther[i] = True
                    count[j] += 1
                    new_candidates.append(j)
            candidates = new_candidates[:]

        print count, knowOther
        # check is there anyone in the 
        for person in xrange(n):
            if count[person] == n-1 and knowOther[person] is False:
                find = True
                for other in xrange(n):
                    if person != other and knows(person, other):
                        find = False
                        break
                if find: return person
        return -1

    #solution2
    def findCelebrity2(self, n):
        candidate = 0
        for i in xrange(1, n):
            # this means original candidate is not valid, since i does not know him, so change candidate to i
            if not knows(i, candidate):
                candidate = i

        # then check whether person from 0 to candidate-1 all knows him and he does not know everyone
        for j in xrange(n):
            if j == candidate:
                continue
            if j < candidate and not knows(j, candidate) or knows(candidate, j):
                return -1
        return candidate

        
if __name__ == "__main__":
    sol = Solution()
    print sol.findCelebrity2(3)
