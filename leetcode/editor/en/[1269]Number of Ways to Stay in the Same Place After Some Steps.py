# You have a pointer at index 0 in an array of size arrLen. At each step, you ca
# n move 1 position to the left, 1 position to the right in the array or stay in t
# he same place (The pointer should not be placed outside the array at any time). 
# 
# 
#  Given two integers steps and arrLen, return the number of ways such that your
#  pointer still at index 0 after exactly steps steps. 
# 
#  Since the answer may be too large, return it modulo 10^9 + 7. 
# 
#  
#  Example 1: 
# 
#  
# Input: steps = 3, arrLen = 2
# Output: 4
# Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
# Right, Left, Stay
# Stay, Right, Left
# Right, Stay, Left
# Stay, Stay, Stay
#  
# 
#  Example 2: 
# 
#  
# Input: steps = 2, arrLen = 4
# Output: 2
# Explanation: There are 2 differents ways to stay at index 0 after 2 steps
# Right, Left
# Stay, Stay
#  
# 
#  Example 3: 
# 
#  
# Input: steps = 4, arrLen = 2
# Output: 8
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= steps <= 500 
#  1 <= arrLen <= 10^6 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        maxLen = min(steps//2 + 1, arrLen)
        dp = [[0]* maxLen for _ in range(steps+1)]
        dp[0][0] = 1
        modulo = 1000000007
        for k in range(1, steps+1):
            for i in range(maxLen):
                dp[k][i] = dp[k-1][i]
                if i>0: dp[k][i] = (dp[k][i] + dp[k-1][i-1]) % modulo
                if i<maxLen-1: dp[k][i] = (dp[k][i] + dp[k-1][i+1]) % modulo
        return dp[steps][0]
# leetcode submit region end(Prohibit modification and deletion)
