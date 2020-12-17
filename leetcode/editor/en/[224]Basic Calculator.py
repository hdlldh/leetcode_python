#Implement a basic calculator to evaluate a simple expression string. 
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces . 
#
# Example 1: 
#
# 
#Input: "1 + 1"
#Output: 2
# 
#
# Example 2: 
#
# 
#Input: " 2-1 + 2 "
#Output: 3 
#
# Example 3: 
#
# 
#Input: "(1+(4+5+2)-3)+(6+8)"
#Output: 23 
#Note:
#
# 
# You may assume that the given expression is always valid. 
# Do not use the eval built-in library function. 
# 
# Related Topics Math Stack



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        num = 0
        ans = 0
        stack = []
        for c in s:
            if c>='0' and c<='9':
                num = num *10 + ord(c) - ord('0')
            elif c == '(':
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif c == ')':
                ans += sign * num
                num = 0
                ans = ans * stack.pop()
                ans = ans + stack.pop()
            elif c in ['+','-']:
                ans += sign * num
                num = 0
                sign = 1 if c=='+' else -1
        ans += sign*num
        return ans

    def calculate1(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        sign = 1
        num = 0
        i = 0
        ans = 0
        while i<n:
            c = s[i]
            if c>='0' and c<='9':
                num = num *10 + ord(c) - ord('0')
            elif c == '(':
                j = i
                bal = 0
                while i<n:
                    if s[i] == '(': bal +=1
                    elif s[i] == ')': bal -=1
                    if bal==0: break
                    i+=1
                num = self.calculate(s[j+1:i])
            if c in ['+','-'] or i==n-1:
                ans += sign * num
                num = 0
                sign = 1 if c=='+' else -1
            i+=1
        return ans


    def calculate2(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        sgn = 1
        num = 0
        res = 0
        for ch in s:
            if ch in '0123456789':
                num = num*10+int(ch)
            elif ch in ['+','-']:
                res += sgn*num
                num = 0
                if ch=='-': sgn = -1
                else: sgn = 1
            elif ch == '(':
                stack.append(res)
                stack.append(sgn)
                res = 0
                sgn = 1
            elif ch== ')':
                res += sgn*num
                num = 0
                res = res * stack.pop()
                res = res + stack.pop()
        res += sgn*num
        return res



#leetcode submit region end(Prohibit modification and deletion)
