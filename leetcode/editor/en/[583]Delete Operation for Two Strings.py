# 
# Given two words word1 and word2, find the minimum number of steps required to 
# make word1 and word2 the same, where in each step you can delete one character i
# n either string.
#  
# 
#  Example 1: 
#  
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make 
# "eat" to "ea".
#  
#  
# 
#  Note: 
#  
#  The length of given words won't exceed 500. 
#  Characters in given words can only be lower-case letters. 
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m==0: return n
        if n==0: return m
        dp = [[0] *(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] +2
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return m+n-dp[m][n]
# leetcode submit region end(Prohibit modification and deletion)
