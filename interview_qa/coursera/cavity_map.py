def cavity(grid):
    n = len(grid)
    for i in xrange(n):
        cur_level = list(grid[i])
        for j in xrange(n):
            if 1 <= i < n-1 and 1 <= j < n-1:
                cur_cell = cur_level[j]
                up, down = grid[i-1][j], grid[i+1][j]
                left, right = grid[i][j-1], grid[i][j+1]
                if all(x != 'X' and x < cur_cell for x in [up, down, left, right]):
                    cur_level[j] = 'X'
        grid[i] = ''.join(cur_level)
        print grid[i]

if __name__ == "__main__":
    cavity(["1112", "1912", "1892", "1234"])
                    
