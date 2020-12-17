# There is a ball in a maze with empty spaces and walls. The ball can go through
#  empty spaces by rolling up, down, left or right, but it won't stop rolling unti
# l hitting a wall. When the ball stops, it could choose the next direction. 
# 
#  Given the ball's start position, the destination and the maze, determine whet
# her the ball could stop at the destination. 
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
# Output: true
# 
# Explanation: One possible way is : left -> down -> left -> down -> right -> do
# wn -> right.
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
# Output: false
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
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n = len(maze), len(maze[0])
        dirs = [-1, 0, 1, 0, -1]
        queue = collections.deque()
        queue.append(start)
        visited = [[0]*n for _ in range(m)]
        visited[start[0]][start[1]] = 1
        while queue:
            ux, uy = queue.popleft()
            if ux==destination[0] and uy==destination[1]: return True
            for k in range(4):
                vx = ux + dirs[k]
                vy = uy + dirs[k + 1]
                while 0<=vx <m and 0<=vy<n and maze[vx][vy]==0:
                    vx += dirs[k]
                    vy += dirs[k + 1]
                vx -= dirs[k]
                vy -= dirs[k+1]
                if visited[vx][vy] == 0:
                    queue.append([vx, vy])
                    visited[vx][vy] = 1
        return False


        
# leetcode submit region end(Prohibit modification and deletion)
