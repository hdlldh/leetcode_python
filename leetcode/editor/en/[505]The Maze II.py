# There is a ball in a maze with empty spaces and walls. The ball can go through
#  empty spaces by rolling up, down, left or right, but it won't stop rolling unti
# l hitting a wall. When the ball stops, it could choose the next direction. 
# 
#  Given the ball's start position, the destination and the maze, find the short
# est distance for the ball to stop at the destination. The distance is defined by
#  the number of empty spaces traveled by the ball from the start position (exclud
# ed) to the destination (included). If the ball cannot stop at the destination, r
# eturn -1. 
# 
#  The maze is represented by a binary 2D array. 1 means the wall and 0 means th
# e empty space. You may assume that the borders of the maze are all walls. The st
# art and destination coordinates are represented by row and column indexes. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input 1: a maze represented by a 2D array
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
# 
# Output: 12
# 
# Explanation: One shortest way is : left -> down -> left -> down -> right -> do
# wn -> right.
#              The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
# 
#  
# 
#  Example 2: 
# 
#  
# Input 1: a maze represented by a 2D array
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
# 
# Output: -1
# 
# Explanation: There is no way for the ball to stop at the destination.
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  There is only one ball and one destination in the maze. 
#  Both the ball and the destination exist on an empty space, and they will not 
# be at the same position initially. 
#  The given maze does not contain border (like the red rectangle in the example
#  pictures), but you could assume the border of the maze are all walls. 
#  The maze contains at least 2 empty spaces, and both the width and height of t
# he maze won't exceed 100. 
#  
#  Related Topics Depth-first Search Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        distance = [[float('inf')] * n for _ in range(m)]
        distance[start[0]][start[1]] = 0
        dirs = [-1, 0, 1, 0, -1]
        queue = collections.deque()
        queue.append(start)
        while queue:
            point = queue.popleft()
            for i in range(4):
                x, y = point[0], point[1]
                dx = dirs[i]
                dy = dirs[i + 1]
                count = 0
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    count += 1
                if distance[point[0]][point[1]] + count < distance[x][y]:
                    distance[x][y] = distance[point[0]][point[1]] + count
                    queue.append([x, y])
        return distance[destination[0]][destination[1]] if distance[destination[0]][destination[1]] < float('inf') else -1
# leetcode submit region end(Prohibit modification and deletion)
