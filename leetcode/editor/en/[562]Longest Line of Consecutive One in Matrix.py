# Given a 01 matrix M, find the longest line of consecutive one in the matrix. T
# he line could be horizontal, vertical, diagonal or anti-diagonal.
# 
#  Example: 
#  
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
#  
#  
# 
#  
# Hint:
# The number of elements in the given matrix will not exceed 10,000.
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m = len(M)
        if m == 0: return 0
        n = len(M[0])
        dp0 = [[0] * n for _ in range(m)]
        dp1 = [[0] * n for _ in range(m)]
        dp2 = [[0] * n for _ in range(m)]
        dp3 = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    dp0[i][j] = 1
                    dp1[i][j] = 1
                    dp2[i][j] = 1
                    dp3[i][j] = 1
                    if i > 0 and j < n - 1:
                        dp3[i][j] = max(dp3[i][j], dp3[i - 1][j + 1] + 1)
                    if i > 0 and j > 0:
                        dp2[i][j] = max(dp2[i][j], dp2[i - 1][j - 1] + 1)
                    if i > 0:
                        dp1[i][j] = max(dp1[i][j], dp1[i - 1][j] + 1)
                    if j > 0:
                        dp0[i][j] = max(dp0[i][j], dp0[i][j - 1] + 1)

                    ans = max(ans, dp0[i][j], dp1[i][j], dp2[i][j], dp3[i][j])
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
