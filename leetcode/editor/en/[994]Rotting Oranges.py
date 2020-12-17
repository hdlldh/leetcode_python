# In a given grid, each cell can have one of three values: 
# 
#  
#  the value 0 representing an empty cell; 
#  the value 1 representing a fresh orange; 
#  the value 2 representing a rotten orange. 
#  
# 
#  Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
#  orange becomes rotten. 
# 
#  Return the minimum number of minutes that must elapse until no cell has a fre
# sh orange. If this is impossible, return -1 instead. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never 
# rotten, because rotting only happens 4-directionally.
#  
# 
#  
#  Example 3: 
# 
#  
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer
#  is just 0.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= grid.length <= 10 
#  1 <= grid[0].length <= 10 
#  grid[i][j] is only 0, 1, or 2. 
#  
#  
#  
#  
#  Related Topics Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m==0: return 0
        n = len(grid[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    grid[i][j] = 2
        step = 0
        dirs = [-1,0,1,0,-1]
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for k in range(4):
                    ti = i+dirs[k]
                    tj = j+dirs[k+1]
                    if ti<0 or ti>=m or tj<0 or tj>=n: continue
                    if grid[ti][tj] ==1:
                        queue.append((ti, tj))
                        grid[ti][tj] = 2
            if queue: step +=1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
        return step
# leetcode submit region end(Prohibit modification and deletion)
