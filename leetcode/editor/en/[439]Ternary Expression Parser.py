# Given a string representing arbitrarily nested ternary expressions, calculate 
# the result of the expression. You can always assume that the given expression is
#  valid and only consists of digits 0-9, ?, :, T and F (T and F represent True an
# d False respectively).
# 
#  Note:
#  
#  The length of the given string is ≤ 10000. 
#  Each number will contain only one digit. 
#  The conditional expressions group right-to-left (as usual in most languages).
#  
#  The condition will always be either T or F. That is, the condition will never
#  be a digit. 
#  The result of the expression will always evaluate to either a digit 0-9, T or
#  F. 
#  
#  
# 
#  
# Example 1:
#  
# Input: "T?2:3"
# 
# Output: "2"
# 
# Explanation: If true, then result is 2; otherwise result is 3.
#  
#  
# 
#  
# Example 2:
#  
# Input: "F?1:T?4:5"
# 
# Output: "4"
# 
# Explanation: The conditional expressions group right-to-left. Using parenthesi
# s, it is read/evaluated as:
# 
#              "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
# 
#           -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
#           -> "4"                                    -> "4"
#  
#  
# 
#  
# Example 3:
#  
# Input: "T?T?F:5:3"
# 
# Output: "F"
# 
# Explanation: The conditional expressions group right-to-left. Using parenthesi
# s, it is read/evaluated as:
# 
#              "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
# 
#           -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
#           -> "F"                                    -> "F"
#  
#  Related Topics Stack Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        for i, ch in enumerate(expression):
            if ch=='?': stack.append(i)

        def eval(expr):
            if len(expr)!=5: return ""
            if expr[0] == 'T':
                return expr[2]
            else:
                return expr[4]

        ans = expression
        while stack:
            i = stack.pop()
            ans = ans[:i-1] + eval(ans[i-1:i+4]) + ans[i+4:]
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)
