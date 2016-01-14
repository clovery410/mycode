import math
class Solution(object):
    def bulbSwitch(self, n):
        bulb = [1 for x in xrange(n)]

        for i in xrange(1, n):
            j = i
            while j < n:
                bulb[j] ^= 1
                j += (i + 1)

        print bulb
        count = 0
        for num in bulb:
            if num == 1:
                count += 1
        return count

    def trickSolution(self, n):
        count = math.sqrt(n)
        
        return int(count)

if __name__ == '__main__':
    sol = Solution()
    print sol.bulbSwitch(10)
    print sol.trickSolution(10)
    sol.bulbSwitch(15)
    sol.bulbSwitch(20)
    sol.bulbSwitch(50)
    sol.bulbSwitch(99)
