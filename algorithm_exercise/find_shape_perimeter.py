from collections import deque
def calPerimeter(matrix, x, y):
    color = matrix[x][y]
    table = [[0 for i in xrange(len(matrix[0]))] for i in xrange(len(matrix))]
    queue = deque(((x, y),))
    while len(queue) > 0:
        (curr_x, curr_y) = queue.popleft()
        table[curr_x][curr_y] = 1
        if curr_x > 0 and matrix[curr_x - 1][curr_y] == color and table[curr_x - 1][curr_y] == 0:
            queue.append((curr_x - 1, curr_y))
        if curr_x < len(matrix) - 1 and matrix[curr_x + 1][curr_y] == color and table[curr_x + 1][curr_y] == 0:
            queue.append((curr_x + 1, curr_y))
        if curr_y > 0 and matrix[curr_x][curr_y - 1] == color and table[curr_x][curr_y - 1] == 0:
            queue.append((curr_x, curr_y - 1))
        if curr_y < len(matrix[0]) - 1 and matrix[curr_x][curr_y + 1] == color and table[curr_x][curr_y + 1] == 0:
            queue.append((curr_x, curr_y + 1))
            
    #calculate perimeter
    perimeter = 0
    for i in xrange(len(table)):
        for j in xrange(len(table[0])):
            if table[i][j] == 1:
                if i == 0 or table[i-1][j] == 0:
                    perimeter += 1
                if i == len(table) - 1 or table[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or table[i][j-1] == 0:
                    perimeter += 1
                if j == len(table[0]) - 1 or table[i][j+1] == 0:
                    perimeter += 1
    return perimeter
print calPerimeter([[1, 0, 1], [0, 1, 1], [0, 0, 1]], 1, 1)
