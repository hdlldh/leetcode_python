#Evaluate the value of an arithmetic expression in Reverse Polish Notation. 
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression. 
#
# Note: 
#
# 
# Division between two integers should truncate toward zero. 
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation. 
# 
#
# Example 1: 
#
# 
#Input: ["2", "1", "+", "3", "*"]
#Output: 9
#Explanation: ((2 + 1) * 3) = 9
# 
#
# Example 2: 
#
# 
#Input: ["4", "13", "5", "/", "+"]
#Output: 6
#Explanation: (4 + (13 / 5)) = 6
# 
#
# Example 3: 
#
# 
#Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
#Output: 22
#Explanation: 
#  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#= ((10 * (6 / (12 * -11))) + 17) + 5
#= ((10 * (6 / -132)) + 17) + 5
#= ((10 * 0) + 17) + 5
#= (0 + 17) + 5
#= 17 + 5
#= 22
# 
# Related Topics Stack



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in ['+','-','*','/']:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+': num = num1+num2
                elif token =='-': num = num2-num1
                elif token =='*': num = num1*num2
                else:
                    sign1 = 1 if num1>=0 else -1
                    sign2 = 1 if num2>=0 else -1
                    if sign1*sign2==1: num = num2//num1
                    elif num2%num1==0: num = num2//num1
                    else: num = num2//num1+1
                stack.append(num)
            else:
                stack.append(int(token))
        return stack[0]

#leetcode submit region end(Prohibit modification and deletion)
