#
#Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
# 
#
# Example 1: 
#Input: 
# 
#"bbbab"
# 
#Output: 
# 
#4
# 
#One possible longest palindromic subsequence is "bbbb".
# 
#
# Example 2: 
#Input:
# 
#"cbbd"
# 
#Output:
# 
#2
# 
#One possible longest palindromic subsequence is "bb".
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        ans = 1
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=1
                    continue
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
        
#leetcode submit region end(Prohibit modification and deletion)
