class SnakeGame(object):
    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snake = [[0,0]]
        self.width = width
        self.height = height
        self.food = food
        self.idx = 0
        self.directions = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        self.score = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        snake = self.snake
        pre_x, pre_y = snake[0]
        cur_x = pre_x + self.directions[direction][0]
        cur_y = pre_y + self.directions[direction][1]
        
        if cur_x < 0 or cur_x >= self.height or cur_y < 0 or cur_y >= self.width or [cur_x, cur_y] in snake[:-1]:
            return -1
        
        if self.idx < len(self.food):
            food_x, food_y = self.food[self.idx]
            if food_x == cur_x and food_y == cur_y and [food_x, food_y] not in snake:
                snake.insert(0, [cur_x, cur_y])
                self.score += 1
                self.idx += 1
                return self.score
        
        for i in reversed(xrange(1, len(snake))):
            snake[i] = snake[i-1]
        snake[0] = [cur_x, cur_y]
        return self.score

#solution2, try to use queue
import collections
class SnakeGame2(object):
    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.food = food
        self.snake = collections.deque([[0, 0]])
        self.directions = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        self.score = 0
        self.food_idx = 0
        
    def move(self, direction):
        snake = self.snake
        pre_x, pre_y = snake[-1]
        cur_x = pre_x + self.directions[direction][0]
        cur_y = pre_y + self.directions[direction][1]

        if cur_x < 0 or cur_x >= self.height or cur_y < 0 or cur_y >= self.width or ([cur_x, cur_y] in snake and [cur_x, cur_y] != snake[0]):
            return -1
        
        snake.append([cur_x, cur_y])
        if self.food_idx < len(self.food) and  [cur_x, cur_y] == self.food[self.food_idx]:
            self.score += 1
            self.food_idx += 1
        else:
            snake.popleft()
        return self.score

#solution3, use a set to speed up the eat body condition check
class SnakeGame3(object):
    def __init__(self, width,height,food):
        self.snake = collections.deque([[0, 0]])
        self.width = width
        self.height = height
        self.food = food
        self.food_idx = 0
        self.directions = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        self.score = 0
        self.usedBlock = {(0,0)}

    def move(self, direction):
        snake = self.snake
        pre_x, pre_y = snake[-1]
        cur_x = pre_x + self.directions[direction][0]
        cur_y = pre_y + self.directions[direction][1]
        tail_x, tail_y = snake[0]

        if cur_x < 0 or cur_x >= self.height or cur_y < 0 or cur_y >= self.width or (cur_x, cur_y) in (self.usedBlock - {(tail_x, tail_y)}):
            return -1

        snake.append([cur_x, cur_y])
        if self.food_idx < len(self.food) and [cur_x, cur_y] == self.food[self.food_idx]:
            self.score += 1
            self.food_idx += 1
        else:
            rm_x, rm_y = snake.popleft()
            self.usedBlock.discard((rm_x, rm_y))
        
        self.usedBlock.add((cur_x, cur_y))
        return self.score
