# Given a positive integer n, break it into the sum of at least two positive int
# egers and maximize the product of those integers. Return the maximum product you
#  can get. 
# 
#  Example 1: 
# 
#  
#  
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1. 
# 
#  
#  Example 2: 
# 
#  
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36. 
# 
#  Note: You may assume that n is not less than 2 and not larger than 58. 
#  
#  Related Topics Math Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n+1)
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]*j, j*(i-j))
        return dp[-1]
        
# leetcode submit region end(Prohibit modification and deletion)
