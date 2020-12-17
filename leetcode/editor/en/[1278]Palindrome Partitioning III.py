# You are given a string s containing lowercase letters and an integer k. You ne
# ed to : 
# 
#  
#  First, change some characters of s to other lowercase English letters. 
#  Then divide s into k non-empty disjoint substrings such that each substring i
# s palindrome. 
#  
# 
#  Return the minimal number of characters that you need to change to divide the
#  string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abc", k = 2
# Output: 1
# Explanation: You can split the string into "ab" and "c", and change 1 characte
# r in "ab" to make it palindrome.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aabbc", k = 3
# Output: 0
# Explanation: You can split the string into "aa", "bb" and "c", all of them are
#  palindrome. 
# 
#  Example 3: 
# 
#  
# Input: s = "leetcode", k = 8
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= s.length <= 100. 
#  s only contains lowercase English letters. 
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        dp = [[float('inf')] * (n+1) for _ in range(k+1)]
        mem = {}
        for k1 in range(1, k+1):
            if k1 == 1:
                for l in range(1,n+1):
                    dp[k1][l] = self.min_cost(s, 0, l-1, mem)
            else:
                for l in range(2, n+1):
                    for j in range(1, l):
                        dp[k1][l] = min(dp[k1][l], dp[k1-1][j] + self.min_cost(s, j, l-1, mem))
        return dp[k][n]

    def min_cost(self, s, i, j, mem):
        if i>=j: return 0
        if (i, j) in mem: return mem[(i, j)]
        ans = self.min_cost(s, i+1, j-1, mem)
        if s[i]!=s[j]: ans += 1
        mem[(i, j)] = ans
        return ans

# leetcode submit region end(Prohibit modification and deletion)
