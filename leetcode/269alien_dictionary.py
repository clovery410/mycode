import collections
class Solution(object):
    def alienOrder(self, words):
        # build the graph by means of in_degree and out_degree
        n = len(words)
        in_degree = collections.defaultdict(list)
        out_degree = collections.defaultdict(int)
        for i in xrange(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            idx1, idx2 = 0, 0
            while idx1 < len(w1) and idx2 < len(w2):
                c1, c2 = w1[idx1], w2[idx2]
                if c1 != c2:
                    out_degree[c1] += 1
                    in_degree[c2].append(c1)
                    break
                idx1 += 1
                idx2 += 1
            # check invalid
            if idx1 < len(w1) and idx2 >= len(w2):
                return ''
                
        # initialize sink nodes
        chars = set(''.join(words))
        sink_nodes = chars - set(out_degree)

        # get topological order
        order = []
        while sink_nodes:
            cur_node = sink_nodes.pop()
            order.append(cur_node)
            for neighbor in in_degree[cur_node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    sink_nodes.add(neighbor)

        # need to check cycle at last, if cycle exist, return empty string means no valid solution
        return ''.join(reversed(order)) if len(order) == len(chars) else ''
        

if __name__ == '__main__':
#    words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
    words = ["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]
    sol = Solution()
    print sol.alienOrder(words)
