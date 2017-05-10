class Solution(object):
    def reconstructQueue(self, people):
        groups = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for person in groups:
            res.insert(person[1], person)
        return res

if __name__ == "__main__":
    sol = Solution()
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print sol.reconstructQueue(people)
        
