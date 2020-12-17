#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. 
#
# Note: You can only move either down or right at any point in time. 
#
# Example: 
#
# 
#Input:
#[
#  [1,3,1],
#  [1,5,1],
#  [4,2,1]
#]
#Output: 7
#Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# Related Topics Array Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: dp[i][j] = grid[i][j]
                else:
                    dp[i][j]=float('inf')
                    if i>0: dp[i][j] = min(dp[i][j],dp[i-1][j]+grid[i][j])
                    if j>0: dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])
        return dp[m-1][n-1]
        
#leetcode submit region end(Prohibit modification and deletion)
