#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000. 
#
# Example 1: 
#
# 
#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.
# 
#
# Example 2: 
#
# 
#Input: "cbbd"
#Output: "bb"
# 
# Related Topics String Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0: return s
        maxLen = 1
        ans = s[0]
        dp = [[False] * n for _ in range(n)]
        for i in range(n): dp[i][i] = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
                if dp[i][i + 1] > maxLen:
                    maxLen = 2
                    ans = s[i:i + 2]
        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > maxLen:
                        maxLen = dp[i][j]
                        ans = s[i:i + l]
        return ans


        
#leetcode submit region end(Prohibit modification and deletion)
