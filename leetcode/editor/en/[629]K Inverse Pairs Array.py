# Given two integers n and k, find how many different arrays consist of numbers 
# from 1 to n such that there are exactly k inverse pairs. 
# 
#  We define an inverse pair as following: For ith and jth element in the array,
#  if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not. 
# 
#  Since the answer may be very large, the answer should be modulo 109 + 7. 
# 
#  Example 1: 
# 
#  
# Input: n = 3, k = 0
# Output: 1
# Explanation: 
# Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inv
# erse pair.
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3, k = 1
# Output: 2
# Explanation: 
# The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The integer n is in the range [1, 1000] and k is in the range [0, 1000]. 
#  
# 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # dp[n][k] = dp[n-1][k] + ... + dp[n-1][k-n+1]
        # dp[n][k+1] = dp[n-1][k+1] + ... + dp[n-1][k-n+2]
        # dp[n][k+1] = dp[n][k] + dp[n-1][k+1] - dp[n-1][k-n+1]
        # dp[n][k] = dp[n][k-1] + dp[n-1][k] - dp[n-1][k-n]
        dp = [[0] *(k+1) for _ in range(n+1)]
        dp[0][0] = 1
        M = 1000000007
        for i in range(1, n+1):
            dp[i][0] = 1
            for j in range(1, k+1):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % M
                if j>=i:
                    dp[i][j] = (dp[i][j] - dp[i-1][j-i] +M)%M
        return dp[n][k]

# leetcode submit region end(Prohibit modification and deletion)
