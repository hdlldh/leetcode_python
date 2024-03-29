# There is a ball in a maze with empty spaces and walls. The ball can go through
#  empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't s
# top rolling until hitting a wall. When the ball stops, it could choose the next 
# direction. There is also a hole in this maze. The ball will drop into the hole i
# f it rolls on to the hole. 
# 
#  Given the ball position, the hole position and the maze, find out how the bal
# l could drop into the hole by moving the shortest distance. The distance is defi
# ned by the number of empty spaces traveled by the ball from the start position (
# excluded) to the hole (included). Output the moving directions by using 'u', 'd'
# , 'l' and 'r'. Since there could be several different shortest ways, you should 
# output the lexicographically smallest way. If the ball cannot reach the hole, ou
# tput "impossible". 
# 
#  The maze is represented by a binary 2D array. 1 means the wall and 0 means th
# e empty space. You may assume that the borders of the maze are all walls. The ba
# ll and the hole coordinates are represented by row and column indexes. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input 1: a maze represented by a 2D array
# 
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
# 
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (0, 1)
# 
# Output: "lul"
# 
# Explanation: There are two shortest ways for the ball to drop into the hole.
# The first way is left -> up -> left, represented by "lul".
# The second way is up -> left, represented by 'ul'.
# Both ways have shortest distance 6, but the first way is lexicographically sma
# ller because 'l' < 'u'. So the output is "lul".
# 
#  
# 
#  Example 2: 
# 
#  
# Input 1: a maze represented by a 2D array
# 
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
# 
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (3, 0)
# 
# Output: "impossible"
# 
# Explanation: The ball cannot reach the hole.
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  There is only one ball and one hole in the maze. 
#  Both the ball and hole exist on an empty space, and they will not be at the s
# ame position initially. 
#  The given maze does not contain border (like the red rectangle in the example
#  pictures), but you could assume the border of the maze are all walls. 
#  The maze contains at least 2 empty spaces, and the width and the height of th
# e maze won't exceed 30. 
#  
#  Related Topics Depth-first Search Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        m, n = len(maze), len(maze[0])
        dists = [[float('inf')]*n for _ in range(m)]
        dirs = [-1, 0, 1, 0, -1]
        way = ['u','r','d','l']
        queue = collections.deque()
        queue.append(ball)
        paths = [['']*n for _ in range(m)]
        dists[ball[0]][ball[1]] = 0
        while queue:
            cur = queue.popleft()
            for i in range(4):
                x, y = cur[0], cur[1]
                dist = dists[x][y]
                path = paths[x][y]
                while x>=0 and x<m and y>=0 and y<n and maze[x][y]==0 and (x!=hole[0] or y!=hole[1]):
                    x += dirs[i]
                    y += dirs[i+1]
                    dist +=1
                if x!=hole[0] or y!=hole[1]:
                    x -= dirs[i]
                    y -= dirs[i+1]
                    dist -= 1
                path = path + way[i]
                if dist < dists[x][y]:
                    dists[x][y] = dist
                    paths[x][y] = path
                    if x != hole[0] or y != hole[1]: queue.append([x, y])
                elif dist == dists[x][y] and path < paths[x][y]:
                    paths[x][y] = path
                    if x!=hole[0] or y!=hole[1]: queue.append([x, y])
        if paths[hole[0]][hole[1]]: return paths[hole[0]][hole[1]]
        return "impossible"

# leetcode submit region end(Prohibit modification and deletion)
