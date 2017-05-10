class Solution(object):
    def readBinaryWatch(self, num):
        def generate(idx, num, hour, minute, all_sols):
            if idx == 10:
                if num == 0:
                    char_hour = str(hour)
                    char_minute = str(minute) if minute >= 10 else '0' + str(minute)
                    all_sols.append(char_hour + ":" + char_minute)
                return
            if num > 0:
                if idx <= 3 and hour + (1 << idx) <= 11:
                    generate(idx+1, num-1, hour + (1 << idx), minute, all_sols)
                elif idx >= 4 and minute + (1 << (idx-4)) <= 59:
                    generate(idx+1, num-1, hour, minute + (1 << (idx-4)), all_sols)
            generate(idx+1, num, hour, minute, all_sols)

        res = []
        generate(0, num, 0, 0, res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.readBinaryWatch(1)
                    
                
