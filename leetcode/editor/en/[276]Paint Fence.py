#There is a fence with n posts, each post can be painted with one of the k colors. 
#
# You have to paint all the posts such that no more than two adjacent fence posts have the same color. 
#
# Return the total number of ways you can paint the fence. 
#
# Note: 
#n and k are non-negative integers. 
#
# Example: 
#
# 
#Input: n = 3, k = 2
#Output: 6
#Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:
#
#            post1  post2  post3      
# -----      -----  -----  -----       
#   1         c1     c1     c2 
#   2         c1     c2     c1 
#   3         c1     c2     c2 
#   4         c2     c1     c1  
#   5         c2     c1     c2
#   6         c2     c2     c1
# 
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        if n == 0: return 0

        dp[1] = k
        if n == 1: return dp[-1]
        dp[2] = k * k
        if n == 2: return dp[-1]
        for i in range(3, n + 1):
            #dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)
            dp[i] = dp[i-2] *(k-1) + (dp[i-1] - dp[i-2]) * k
        return dp[-1]
        
#leetcode submit region end(Prohibit modification and deletion)
