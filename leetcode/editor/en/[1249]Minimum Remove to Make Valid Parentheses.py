#Given a string s of '(' , ')' and lowercase English characters. 
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any 
#positions ) so that the resulting parentheses string is valid and return any val
#id string. 
#
# Formally, a parentheses string is valid if and only if: 
#
# 
# It is the empty string, contains only lowercase characters, or 
# It can be written as AB (A concatenated with B), where A and B are valid strin
#gs, or 
# It can be written as (A), where A is a valid string. 
# 
#
# 
# Example 1: 
#
# 
#Input: s = "lee(t(c)o)de)"
#Output: "lee(t(c)o)de"
#Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# 
#
# Example 2: 
#
# 
#Input: s = "a)b(c)d"
#Output: "ab(c)d"
# 
#
# Example 3: 
#
# 
#Input: s = "))(("
#Output: ""
#Explanation: An empty string is also valid.
# 
#
# Example 4: 
#
# 
#Input: s = "(a(b(c)d)"
#Output: "a(b(c)d)"
# 
#
# 
# Constraints: 
#
# 
# 1 <= s.length <= 10^5 
# s[i] is one of '(' , ')' and lowercase English letters. 
# Related Topics String Stack




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        toRemove = set()
        for i, ch in enumerate(s):
            if ch=='(':
                stack.append(i)
            elif ch==')':
                if not stack: toRemove.add(i)
                else: stack.pop()
        for i in stack: toRemove.add(i);
        ans = ""
        for i, ch in enumerate(s):
            if i not in toRemove: ans += ch
        return ans


        
#leetcode submit region end(Prohibit modification and deletion)
