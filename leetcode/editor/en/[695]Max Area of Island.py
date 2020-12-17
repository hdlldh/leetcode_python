#Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. 
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.) 
#
# Example 1: 
#
# 
#[[0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
#Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
#
# Example 2: 
#
# 
#[[0,0,0,0,0,0,0,0]] 
#Given the above grid, return 0.
#
# Note: The length of each dimension in the given grid does not exceed 50. 
# Related Topics Array Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        m = len(grid)
        if m==0: return ans
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: ans = max(ans, self.dfs(grid, i, j))
        return ans

    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i<0 or i>=m or j<0 or j>=n: return 0
        if grid[i][j]!= 1: return 0
        grid[i][j] = -1
        ans = 1
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        for k in range(4):
            ans += self.dfs(grid, i+dx[k], j+dy[k])
        return ans


        
#leetcode submit region end(Prohibit modification and deletion)
