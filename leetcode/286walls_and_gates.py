from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        INF = 2 ** 31 - 1
        m, n = len(rooms), len(rooms[0]) if len(rooms) > 0 else 0
        queue = deque([])
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        path = 0
        while queue:
            length = len(queue)
            for x in xrange(length):
                cur_i, cur_j = queue.popleft()
                if rooms[cur_i][cur_j] == INF:
                    rooms[cur_i][cur_j] = path
                for offset_i, offset_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_i, next_j = cur_i + offset_i, cur_j + offset_j
                    if 0 <= next_i < m and 0 <= next_j < n and rooms[next_i][next_j] == INF:
                        queue.append((next_i, next_j))
            path += 1

        return rooms

if __name__ == "__main__":
    INF = 2 ** 31 - 1
    sol = Solution()
    rooms = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]
    print sol.wallsAndGates(rooms)
                                
                
