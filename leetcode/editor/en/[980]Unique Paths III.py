# On a 2-dimensional grid, there are 4 types of squares: 
# 
#  
#  1 represents the starting square. There is exactly one starting square. 
#  2 represents the ending square. There is exactly one ending square. 
#  0 represents empty squares we can walk over. 
#  -1 represents obstacles that we cannot walk over. 
#  
# 
#  Return the number of 4-directional walks from the starting square to the endi
# ng square, that walk over every non-obstacle square exactly once. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2) 
# 
#  
#  Example 2: 
# 
#  
# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3) 
# 
#  
#  Example 3: 
# 
#  
# Input: [[0,1],[2,0]]
# Output: 0
# Explanation: 
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
#  
#  
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= grid.length * grid[0].length <= 20 
#  Related Topics Backtracking Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        start, end, p = None, None, 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: start = (i,j)
                elif grid[i][j] == 2: end = (i, j)
                elif grid[i][j] == 0: p += 1

        dirs = [-1, 0, 1, 0, -1]
        def dfs(grid, i, j, p):
            if i<0 or i>=m or j<0 or j>=n: return 0
            if grid[i][j] <0: return 0
            if (i, j) == end and p==0: return 1
            grid[i][j] = -1
            ans = dfs(grid, i+1, j, p-1)+ dfs(grid, i-1, j, p-1) + dfs(grid, i, j+1, p-1) + dfs(grid, i, j-1, p-1)
            grid[i][j] = 0
            return ans

        return dfs(grid, start[0], start[1], p)


        
# leetcode submit region end(Prohibit modification and deletion)
