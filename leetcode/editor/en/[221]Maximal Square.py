#Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area. 
#
# Example: 
#
# 
#Input: 
#
#1 0 1 0 0
#1 0 1 1 1
#1 1 1 1 1
#1 0 0 1 0
#
#Output: 4
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m==0:return 0
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] =='0': continue
                dp[i][j] = 1
                if i>0 and j>0: dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                ans = max(ans, dp[i][j])
        return ans*ans
        
#leetcode submit region end(Prohibit modification and deletion)
