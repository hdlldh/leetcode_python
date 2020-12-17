#Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (re
#presenting land) connected 4-directionally (horizontal or vertical.) You may ass
#ume all four edges of the grid are surrounded by water. 
#
# Count the number of distinct islands. An island is considered to be the same a
#s another if and only if one island can be translated (and not rotated or reflec
#ted) to equal the other. 
#
# Example 1: 
# 
#11000
#11000
#00011
#00011
# 
#Given the above grid map, return 1.
# 
#
# Example 2: 
# 11011
#10000
#00001
#11011 
#Given the above grid map, return 3. 
#Notice that:
# 
#11
#1
# 
#and
# 
# 1
#11
# 
#are considered different island shapes, because we do not consider reflection /
# rotation.
# 
#
# Note:
#The length of each dimension in the given grid does not exceed 50.
# Related Topics Hash Table Depth-first Search




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        seen = [[0]*n for _ in range(m)]
        ans = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and seen[i][j]!=1:
                    shape = []
                    self.dfs(grid, seen, i, j, i, j, shape)
                    ans.add(tuple(shape))
        return len(ans)

    def dfs(self, grid, seen, i, j, i0, j0, shape):
        m, n = len(grid), len(grid[0])
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0 or seen[i][j]==1: return
        shape.extend([i-i0, j-j0])
        seen[i][j] =1
        dirs = [-1, 0, 1, 0, -1]
        for k in range(4):
            self.dfs(grid, seen, i+dirs[k], j+dirs[k+1], i0, j0, shape)

#leetcode submit region end(Prohibit modification and deletion)
