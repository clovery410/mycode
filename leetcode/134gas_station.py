class Solution(object):
    #solution1, original solution
    def canCompleteCircuit(self, gas, cost):
        l = len(gas)
        diff = [gas[x] - cost[x] for x in range(l)]

        #early stop
        if sum(diff) < 0:
            return -1
        
        #check with the next number after smallest number first, since this has larger chance
        smallest = min(diff)
        i = (diff.index(smallest) + 1) % l
        for _ in range(l):
            num = diff[i]
            if num >= 0:
                total = 0
                for j in range(l):
                    total += diff[(i+j)%l]
                    if total < 0:
                        break
                if j == l-1 and total >=0: 
                    return i
            i = (i + 1) % l
        return -1

    #solution2, use the idea of checking the accumulate sum, if the total sum < 0, then there is no solution, otherwise, just find the minimum accumulate sum's position, the starting point should be the next index.
    #This solution's time complexcity is O(n), but still uses O(n) extra space, following solution improved the space complexcity
    def canCompleteCircuit(self, gas, cost):
        l = len(gas)
        accum = [gas[x] - cost[x] for x in range(l)]
        for i in xrange(1, l):
            accum[i] += accum[i-1]

        if l == 0 or accum[-1] < 0:
            return -1
        
        min_val = min(accum)
        min_idx = accum.index(min_val)
        return (min_idx+1) % l

    #solution3, optimize solution2 by improving space complexcity to O(1)
    def canCompleteCircuit(self, gas, cost):
        l = len(gas)
        idx, min_val = -1, sys.maxint
        accu_total = 0
        for i in xrange(l):
            cur_diff = gas[i] - cost[i]
            accu_total += cur_diff
            if accu_total  < min_val:
                min_val = accu_total
                idx = (i + 1) % l
        return idx

    #solution4, briliant solution
    def canCompleteCircuit4(self, gas, cost):
        s, e = len(gas) - 1, 0
        accu_sum = gas[s] - cost[s]
        while e < s:
            if accu_sum >= 0:
                accu_sum += gas[e] - cost[e]
                e += 1
            else:
                s -= 1
                accu_sum += gas[s] - cost[s]

        return -1 if accu_sum < 0 else s
        
        
