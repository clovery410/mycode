import collections
class Solution(object):
    def alienOrder(self, words):
        # initialize the graph
        in_degree = collections.defaultdict(list)
        out_degree = collections.defaultdict(int)

        # build the graph
        for i in xrange(1, len(words)):
            w1, w2 = words[i-1], words[i]
            j = 0
            while j < len(w1) and j < len(w2) and w1[j] == w2[j]:
                j += 1
            if j == len(w1):
                continue
            elif j == len(w2):
                return ''
            else:
                in_degree[w2[j]].append(w1[j])
                out_degree[w1[j]] += 1

        # initialize sink nodes
        res = []
        chars = set(''.join(words))
        sinks = chars - set(out_degree)

        # get topological order
        while sinks:
            cur = sinks.pop()
            res.append(cur)
            for neighbor in in_degree[cur]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    sinks.add(neighbor)
                    
        return ''.join(res[::-1]) if len(res) == len(chars) else ''

if __name__ == "__main__":
    sol = Solution()
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print sol.alienOrder(words)
        
