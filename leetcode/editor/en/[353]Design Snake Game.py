#Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game. 
#
# The snake is initially positioned at the top left corner (0,0) with length = 1 unit. 
#
# You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1. 
#
# Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake. 
#
# When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake. 
#
# Example: 
#
# 
#Given width = 3, height = 2, and food = [[1,2],[0,1]].
#
#Snake snake = new Snake(width, height, food);
#
#Initially the snake appears at position (0,0) and the food at (1,2).
#
#|S| | |
#| | |F|
#
#snake.move("R"); -> Returns 0
#
#| |S| |
#| | |F|
#
#snake.move("D"); -> Returns 0
#
#| | | |
#| |S|F|
#
#snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )
#
#| |F| |
#| |S|S|
#
#snake.move("U"); -> Returns 1
#
#| |F|S|
#| | |S|
#
#snake.move("L"); -> Returns 2 (Snake eats the second food)
#
#| |S|S|
#| | |S|
#
#snake.move("U"); -> Returns -1 (Game over because snake collides with border)
# 
# Related Topics Design Queue

import collections

#leetcode submit region begin(Prohibit modification and deletion)
class SnakeGame(object):

    def __init__(self, width, height, food):
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
        self.width = width
        self.height = height
        self.food = collections.deque(food)
        self.trace = collections.deque(());
        self.trace.append((0,0))
        self.body = set()
        self.body.add((0,0))
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
        hy, hx = self.trace[0]
        if direction == 'U':
            hy -= 1
        elif direction == 'D':
            hy += 1
        elif direction == 'L':
            hx -= 1
        else:
            hx += 1
        if hx < 0 or hx >= self.width or hy < 0 or hy >= self.height: return -1
        tail = self.trace.pop()
        self.body.remove(tail)
        if (hy, hx) in self.body: return -1
        if self.food and [hy, hx] == self.food[0]:
            self.score += 1
            self.trace.append(tail)
            self.body.add(tail)
            self.food.popleft()
        self.trace.appendleft((hy, hx))
        self.body.add((hy, hx))
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
#leetcode submit region end(Prohibit modification and deletion)
