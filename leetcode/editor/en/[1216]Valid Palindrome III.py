# Given a string s and an integer k, find out if the given string is a K-Palindr
# ome or not. 
# 
#  A string is K-Palindrome if it can be transformed into a palindrome by removi
# ng at most k characters from it. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcdeca", k = 2
# Output: true
# Explanation: Remove 'b' and 'e' characters.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s has only lowercase English letters. 
#  1 <= k <= s.length 
#  
#  Related Topics String Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        return self.dfs(s, 0, len(s)-1, {}) <=k

    def dfs(self, s, left, right, mem):
        if left==right: return 0
        if left+1==right and s[left]==s[right]: return 0
        if (left, right) in mem: return mem[(left, right)]
        if s[left] == s[right]:
            mem[(left, right)] = self.dfs(s, left+1, right-1, mem)
        else:
            mem[(left, right)] = min(self.dfs(s, left + 1, right, mem), self.dfs(s, left, right - 1, mem)) + 1
        return mem[(left, right)]
# leetcode submit region end(Prohibit modification and deletion)
