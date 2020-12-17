#Implement a basic calculator to evaluate a simple expression string. 
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero. 
#
# Example 1: 
#
# 
#Input: "3+2*2"
#Output: 7
# 
#
# Example 2: 
#
# 
#Input: " 3/2 "
#Output: 1 
#
# Example 3: 
#
# 
#Input: " 3+5 / 2 "
#Output: 5
# 
#
# Note: 
#
# 
# You may assume that the given expression is always valid. 
# Do not use the eval built-in library function. 
# 
# Related Topics String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        sign = '+'
        num = 0
        i = 0
        ans = 0
        cur = 0
        while i < n:
            c = s[i]
            if c>='0' and c<='9':
                num = num *10 + ord(c) -ord('0')
            if c in ['+','-','*','/'] or i == n-1:
                if sign == '+': cur += num
                elif sign == '-': cur -= num
                elif sign == '*': cur *= num
                elif sign == '/':
                    if cur * num >= 0: cur = cur //num
                    elif cur % num == 0:cur = cur // num
                    else: cur = cur // num + 1
                if c in ['+','-'] or i == n-1:
                    ans += cur
                    cur = 0
                sign = c
                num = 0
            i+=1
        return ans

#leetcode submit region end(Prohibit modification and deletion)
