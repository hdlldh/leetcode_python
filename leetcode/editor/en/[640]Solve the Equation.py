# 
# Solve a given equation and return the value of x in the form of string "x=#val
# ue". The equation contains only '+', '-' operation, the variable x and its coeff
# icient.
#  
# 
#  
# If there is no solution for the equation, return "No solution".
#  
#  
# If there are infinite solutions for the equation, return "Infinite solutions".
# 
#  
#  
# If there is exactly one solution for the equation, we ensure that the value of
#  x is an integer.
#  
# 
#  Example 1: 
#  
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"
#  
#  
# 
#  Example 2: 
#  
# Input: "x=x"
# Output: "Infinite solutions"
#  
#  
# 
#  Example 3: 
#  
# Input: "2x=x"
# Output: "x=0"
#  
#  
# 
#  Example 4: 
#  
# Input: "2x+3x-6x=x+2"
# Output: "x=-1"
#  
#  
# 
#  Example 5: 
#  
# Input: "x=x+2"
# Output: "No solution"
#  
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        l = self.parse(left)
        r = self.parse(right)
        print(l, r)
        if l[0] == r[0]:
            return 'Infinite solutions' if l[1] == r[1] else 'No solution'
        return 'x=%s' % ((l[1] - r[1]) // (r[0] - l[0]))

    def parse(self, equ):
        op = '+'
        num = 0
        ans = [0, 0]
        for i, ch in enumerate(equ):
            if ch in '0123456789':
                num = num * 10 + int(ch)
            elif ch == 'x':
                if num == 0 and (i == 0 or equ[i - 1] != '0'): num = 1
                if op == '+':
                    ans[0] += num
                else:
                    ans[0] -= num
                num = 0
            elif ch in ['+', '-']:
                if op == '+':
                    ans[1] += num
                else:
                    ans[1] -= num
                op = ch
                num = 0
        if num > 0:
            if op == '+':
                ans[1] += num
            else:
                ans[1] -= num

        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
