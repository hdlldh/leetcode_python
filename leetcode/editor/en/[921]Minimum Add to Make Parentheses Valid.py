# Given a string S of '(' and ')' parentheses, we add the minimum number of pare
# ntheses ( '(' or ')', and in any positions ) so that the resulting parentheses s
# tring is valid. 
# 
#  Formally, a parentheses string is valid if and only if: 
# 
#  
#  It is the empty string, or 
#  It can be written as AB (A concatenated with B), where A and B are valid stri
# ngs, or 
#  It can be written as (A), where A is a valid string. 
#  
# 
#  Given a parentheses string, return the minimum number of parentheses we must 
# add to make the resulting string valid. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: "())"
# Output: 1
#  
# 
#  
#  Example 2: 
# 
#  
# Input: "((("
# Output: 3
#  
# 
#  
#  Example 3: 
# 
#  
# Input: "()"
# Output: 0
#  
# 
#  
#  Example 4: 
# 
#  
# Input: "()))(("
# Output: 4 
# 
#  
#  
#  
#  
# 
#  Note: 
# 
#  
#  S.length <= 1000 
#  S only consists of '(' and ')' characters. 
#  
# 
#  
#  
#  
#  
#  
#  
#  Related Topics Stack Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        ans = 0
        bal = 0
        for ch in S:
            if ch=='(': bal +=1
            else: bal -= 1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal
        
# leetcode submit region end(Prohibit modification and deletion)
