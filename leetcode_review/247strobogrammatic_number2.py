class Solution(object):
    def findStrobogrammatic(self, n):
        def generate(num):
            if num == 0:
                return ['']
            if num == 1:
                return ["0", "1", "8"]
            res = []
            candidate = {"1": "1", "6": "9", "8": "8", "9": "6"}
            if num < n:
                candidate["0"] = "0"
            inner = generate(num-2)
            for key, val in candidate.items():
                res.extend([key + elem + val for elem in inner])
            return res

        return generate(n)

if __name__ == "__main__":
    sol = Solution()
    print sol.findStrobogrammatic(1)
        
