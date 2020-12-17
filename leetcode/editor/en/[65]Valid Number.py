#Validate if a given string can be interpreted as a decimal number. 
#
# Some examples: 
#"0" => true 
#" 0.1 " => true 
#"abc" => false 
#"1 a" => false 
#"2e10" => true 
#" -90e3 " => true 
#" 1e" => false 
#"e3" => false 
#" 6e-1" => true 
#" 99e2.5 " => false 
#"53.5e93" => true 
#" --6 " => false 
#"-+3" => false 
#"95a54e53" => false 
#
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number: 
#
# 
# Numbers 0-9 
# Exponent - "e" 
# Positive/negative sign - "+"/"-" 
# Decimal point - "." 
# 
#
# Of course, the context of these characters also matters in the input. 
#
# Update (2015-02-10): 
#The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition. 
# Related Topics Math String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        INVALID = 0
        SPACE = 1
        SIGN = 2
        DIGIT = 3
        DOT = 4
        EXPONENT = 5

        trans_table =  [
            # 0. Invalid, 1. Space, 2. Sign, 3. Digit, 4. Dot, 5. Expoent
            [-1, 0, 3, 1, 2, -1], # 0. initial state or only space
            [-1, 8, -1, 1, 4, 5], # 1. contain digits only
            [-1, -1, -1, 4, -1, -1], # 2. contain dot without digit
            [-1, -1, -1, 1, 2, -1], # 3. contain sign
            [-1, 8, -1, 4, -1, 5], # 4. contain valid number
            [-1, -1, 6, 7, -1, -1], # 5. contain valid number and exponent
            [-1, -1, -1, 7, -1, -1], # 6. contain exponent and sign
            [-1, 8, -1, 7, -1, -1], # 7. contain exponent, sign and digit
            [-1, 8, -1, -1, -1, -1] # 8. contain valid number and followed by a space
        ]
        state = 0
        for ch in s:
            if ch ==' ': next_state = trans_table[state][SPACE]
            elif ch in ['+', '-']: next_state = trans_table[state][SIGN]
            elif ch.isdigit(): next_state = trans_table[state][DIGIT]
            elif ch == '.': next_state = trans_table[state][DOT]
            elif ch in ['E', 'e']: next_state = trans_table[state][EXPONENT]
            else: next_state = trans_table[state][INVALID]
            if next_state == -1: return False
            state = next_state

        return state in [1, 4, 7, 8]
#leetcode submit region end(Prohibit modification and deletion)
