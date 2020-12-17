#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
#
# An input string is valid if: 
#
# 
# Open brackets must be closed by the same type of brackets. 
# Open brackets must be closed in the correct order. 
# 
#
# Note that an empty string is also considered valid. 
#
# Example 1: 
#
# 
#Input: "()"
#Output: true
# 
#
# Example 2: 
#
# 
#Input: "()[]{}"
#Output: true
# 
#
# Example 3: 
#
# 
#Input: "(]"
#Output: false
# 
#
# Example 4: 
#
# 
#Input: "([)]"
#Output: false
# 
#
# Example 5: 
#
# 
#Input: "{[]}"
#Output: true
# 
# Related Topics String Stack



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {')':'(',']':'[','}':'{'}
        stack = []
        for symbol in s:
            if symbol not in pairs:
                stack.append(symbol)
            else:
                if stack and pairs[symbol]==stack[-1]:
                    stack.pop()
                else: return False
        return len(stack) == 0

#leetcode submit region end(Prohibit modification and deletion)
