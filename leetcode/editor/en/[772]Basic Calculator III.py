# Implement a basic calculator to evaluate a simple expression string. 
# 
#  The expression string may contain open ( and closing parentheses ), the plus 
# + or minus sign -, non-negative integers and empty spaces . 
# 
#  The expression string contains only non-negative integers, +, -, *, / operato
# rs , open ( and closing parentheses ) and empty spaces . The integer division sh
# ould truncate toward zero. 
# 
#  You may assume that the given expression is always valid. All intermediate re
# sults will be in the range of [-2147483648, 2147483647]. 
# 
#  Some examples: 
# 
#  
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
#  
# 
#  
# 
#  Note: Do not use the eval built-in library function. 
#  Related Topics String Stack


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cur = 0
        ans = 0
        num = 0
        op = '+'
        i = 0
        while i <n:
            c = s[i]
            if c>='0' and c<='9':
                num = num * 10 + ord(c) - ord('0')
            elif c=='(':
                j = i
                bal = 0
                while i <n:
                    if s[i]=='(': bal+=1
                    elif s[i]==')':bal-=1
                    if bal ==0: break
                    i+= 1
                num = self.calculate(s[j+1:i])

            if c in ['+','-','*','/'] or i==n-1:
                if op=='+': cur += num
                elif op=='-': cur -= num
                elif op=='*': cur *= num
                elif op=='/':
                    if cur * num >= 0:cur = cur // num
                    elif cur % num == 0:cur = cur // num
                    else:cur = cur // num + 1
                if c in ['+','-'] or i == n-1:
                    ans += cur
                    cur = 0
                op = c
                num = 0
            i += 1
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)
