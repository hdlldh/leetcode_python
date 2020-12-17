# Given a 2D grid consists of 0s (land) and 1s (water). An island is a maximal 4
# -directionally connected group of 0s and a closed island is an island totally (a
# ll left, top, right, bottom) surrounded by 1s. 
# 
#  Return the number of closed islands. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,
# 0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (gr
# oup of 1s). 
# 
#  Example 2: 
# 
#  
# 
#  
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= grid.length, grid[0].length <= 100 
#  0 <= grid[i][j] <=1 
#  Related Topics Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.isOpen = False
                    self.dfs(grid, i, j)
                    if not self.isOpen:
                        ans += 1
        return ans

    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i<0 or i>=m or j<0 or j>=n:
            self.isOpen = True
            return
        if grid[i][j] == 1: return
        grid[i][j] = 1
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)

        
# leetcode submit region end(Prohibit modification and deletion)
