#
#Given a string containing only three types of characters: '(', ')' and '*', wri
#te a function to check whether this string is valid. We define the validity of a
# string by these rules:
# 
# Any left parenthesis '(' must have a corresponding right parenthesis ')'. 
# Any right parenthesis ')' must have a corresponding left parenthesis '('. 
# Left parenthesis '(' must go before the corresponding right parenthesis ')'. 
# '*' could be treated as a single right parenthesis ')' or a single left parent
#hesis '(' or an empty string. 
# An empty string is also valid. 
# 
# 
#
# Example 1: 
# 
#Input: "()"
#Output: True
# 
# 
#
# Example 2: 
# 
#Input: "(*)"
#Output: True
# 
# 
#
# Example 3: 
# 
#Input: "(*))"
#Output: True
# 
# 
#
# Note: 
# 
# The string size will be in the range [1, 100]. 
# 
# Related Topics String




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        b = 0
        for i in range(n):
            if s[i]!=')': b+=1
            else: b-=1
            if b<0: return False
        b = 0
        for i in range(n-1, -1, -1):
            if s[i]!='(': b+=1
            else: b-=1
            if b<0: return False
        return True

#leetcode submit region end(Prohibit modification and deletion)
