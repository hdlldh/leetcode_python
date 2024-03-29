#A message containing letters from A-Z is being encoded to numbers using the following mapping: 
#
# 
#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
# 
#
# Given a non-empty string containing only digits, determine the total number of ways to decode it. 
#
# Example 1: 
#
# 
#Input: "12"
#Output: 2
#Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
#
# Example 2: 
#
# 
#Input: "226"
#Output: 3
#Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6). 
# Related Topics String Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            if s[i-1]!="0": dp[i] += dp[i-1]
            if i>1 and s[i-2:i]<="26" and s[i-2:i]>="10": dp[i] += dp[i-2]
        return dp[-1]
        
#leetcode submit region end(Prohibit modification and deletion)
