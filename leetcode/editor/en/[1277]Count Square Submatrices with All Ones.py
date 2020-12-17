# Given a m * n matrix of ones and zeros, return how many square submatrices hav
# e all ones. 
# 
#  
#  Example 1: 
# 
#  
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 300 
#  1 <= arr[0].length <= 300 
#  0 <= arr[i][j] <= 1 
#  
#  Related Topics Array Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m==0: return 0
        n = len(matrix[0])
        k = min(m, n)
        dp = [[[0]*n for _ in xrange(m)] for _ in xrange(k+1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[1][i][j] = 1
                    ans +=1
        for l in range(2, k+1):
            for i in range(1,m):
                for j in range(1,n):
                    if matrix[i][j]==1 and dp[l-1][i-1][j]==1 and dp[l-1][i][j-1] ==1 and dp[l-1][i-1][j-1] ==1:
                        dp[l][i][j] =1
                        ans +=1
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
