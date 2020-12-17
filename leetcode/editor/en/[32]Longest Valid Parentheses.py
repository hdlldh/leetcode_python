#Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring. 
#
# Example 1: 
#
# 
#Input: "(()"
#Output: 2
#Explanation: The longest valid parentheses substring is "()"
# 
#
# Example 2: 
#
# 
#Input: ")()())"
#Output: 4
#Explanation: The longest valid parentheses substring is "()()"
# 
# Related Topics String Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        ans = 0
        for i, sym in enumerate(s):
            if sym == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        ans = max(ans, i - stack[-1])
                    else:
                        stack.append(i)
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
