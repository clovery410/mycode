import collections
class Solution(object):
    def isWayOut(self, maze, start_point, end_point):
        m, n = len(maze), len(maze[0]) if len(maze) else 0
        queue = collections.deque([start_point])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            cur_i, cur_j = queue.popleft()
            visited.add((cur_i, cur_j))
            if (cur_i, cur_j) == end_point:
                return True
            for diff_i, diff_j in directions:
                new_i, new_j = cur_i + diff_i, cur_j + diff_j
                if 0 <= new_i < m and 0 <= new_j < n and maze[new_i][new_j] == 0 and (new_i, new_j) not in visited:
                    queue.append((new_i, new_j))
        return False
        
    def findWayOut(self, maze, start_point, end_point):
        def generatePath(children, start_point, end_point):
            if start_point == end_point:
                res.append(path[:])
                return
            for child in children[start_point]:
                path.append(child)
                generatePath(children, child, end_point)
                path.pop()
                
        m, n = len(maze), len(maze[0]) if len(maze) else 0
        queue = collections.deque([start_point])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        children = collections.defaultdict(list)
        path = [start_point]
        res = []
        done = False
        
        while queue:
            cur_i, cur_j = queue.popleft()
            visited.add((cur_i, cur_j))
            if (cur_i, cur_j) == end_point:
                done = True
                break
            for diff_i, diff_j in directions:
                new_i, new_j = cur_i + diff_i, cur_j + diff_j
                if 0 <= new_i < m and 0 <= new_j < n and maze[new_i][new_j] == 0 and (new_i, new_j) not in visited:
                    queue.append((new_i, new_j))
                    children[(cur_i, cur_j)].append((new_i, new_j))

        if done:
            generatePath(children, start_point, end_point)
        return res

if __name__ == "__main__":
    sol = Solution()
    maze = [[1,0,0,0],[0,0,1,0],[0,0,1,0],[0,1,0,0]]
    print sol.findWayOut(maze, (1,0), (3,2))
