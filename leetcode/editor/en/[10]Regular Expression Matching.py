#Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'. 
#
# 
#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
# 
#
# The matching should cover the entire input string (not partial). 
#
# Note: 
#
# 
# s could be empty and contains only lowercase letters a-z. 
# p could be empty and contains only lowercase letters a-z, and characters like . or *. 
# 
#
# Example 1: 
#
# 
#Input:
#s = "aa"
#p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".
# 
#
# Example 2: 
#
# 
#Input:
#s = "aa"
#p = "a*"
#Output: true
#Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# 
#
# Example 3: 
#
# 
#Input:
#s = "ab"
#p = ".*"
#Output: true
#Explanation: ".*" means "zero or more (*) of any character (.)".
# 
#
# Example 4: 
#
# 
#Input:
#s = "aab"
#p = "c*a*b"
#Output: true
#Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# 
#
# Example 5: 
#
# 
#Input:
#s = "mississippi"
#p = "mis*is*p*."
#Output: false
# 
# Related Topics String Dynamic Programming Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] *(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] != '*':
                    dp[i][j] = i>0 and dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')
                else:
                    if j>1:
                        dp[i][j] = dp[i][j-2] or (i>0 and dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
        return dp[m][n]

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return True if not s else False
        ans = False
        if len(p) > 1 and p[1] == '*':
            ans = self.isMatch(s, p[2:])
            if s:
                firstMatch = s[0] == p[0] or p[0] == '.'
                ans = ans or firstMatch and self.isMatch(s[1:], p)
        else:
            if s:
                firstMatch = s[0] == p[0] or p[0] == '.'
                ans = ans or firstMatch and self.isMatch(s[1:], p[1:])
        return ans

        
#leetcode submit region end(Prohibit modification and deletion)
