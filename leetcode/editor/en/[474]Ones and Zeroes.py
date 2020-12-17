# Given an array, strs, with strings consisting of only 0s and 1s. Also two inte
# gers m and n. 
# 
#  Now your task is to find the maximum number of strings that you can form with
#  given m 0s and n 1s. Each 0 and 1 can be used at most once. 
# 
#  
#  Example 1: 
# 
#  
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: This are totally 4 strings can be formed by the using of 5 0s and
#  3 1s, which are "10","0001","1","0".
#  
# 
#  Example 2: 
# 
#  
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: You could form "10", but then you'd have nothing left. Better for
# m "0" and "1".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 600 
#  1 <= strs[i].length <= 100 
#  strs[i] consists only of digits '0' and '1'. 
#  1 <= m, n <= 100 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            zeros = 0
            ones = 0
            for ch in s:
                if ch=='0':zeros+=1
                else: ones+=1
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i>=zeros and j>=ones:
                        dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[m][n]
        
# leetcode submit region end(Prohibit modification and deletion)
