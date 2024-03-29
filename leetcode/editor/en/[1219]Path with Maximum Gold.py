# In a gold mine grid of size m * n, each cell in this mine has an integer repre
# senting the amount of gold in that cell, 0 if it is empty. 
# 
#  Return the maximum amount of gold you can collect under the conditions: 
# 
#  
#  Every time you are located in a cell you will collect all the gold in that ce
# ll. 
#  From your position you can walk one step to the left, right, up or down. 
#  You can't visit the same cell more than once. 
#  Never visit a cell with 0 gold. 
#  You can start and stop collecting gold from any position in the grid that has
#  some gold. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# Explanation:
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= grid.length, grid[i].length <= 15 
#  0 <= grid[i][j] <= 100 
#  There are at most 25 cells containing gold. 
#  Related Topics Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        self.ans = 0
        for i in range(m):
            for j in range(n):
                self.dfs(grid, i, j, 0)
        return self.ans

    def dfs(self, grid, i, j, out):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n: return
        if grid[i][j] == 0:
            self.ans = max(self.ans, out)
            return
        dirs = [-1, 0, 1, 0, -1]
        val = grid[i][j]
        grid[i][j] = 0
        for d in range(4):
            self.dfs(grid, i + dirs[d], j + dirs[d + 1], out + val)
        grid[i][j] = val
        
# leetcode submit region end(Prohibit modification and deletion)
