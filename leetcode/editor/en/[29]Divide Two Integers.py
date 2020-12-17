#Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator. 
#
# Return the quotient after dividing dividend by divisor. 
#
# The integer division should truncate toward zero. 
#
# Example 1: 
#
# 
#Input: dividend = 10, divisor = 3
#Output: 3 
#
# Example 2: 
#
# 
#Input: dividend = 7, divisor = -3
#Output: -2 
#
# Note: 
#
# 
# Both dividend and divisor will be 32-bit signed integers. 
# The divisor will never be 0. 
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows. 
# 
# Related Topics Math Binary Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign1 = 1 if dividend >= 0 else -1
        sign2 = 1 if divisor >= 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend< divisor: return 0

        low = 0
        high = dividend
        while low <= high:
            mid = low + (high-low)//2
            if divisor*mid > dividend: high = mid -1
            else: low = mid +1
        if sign1*sign2<0: return max(-high, -2**31)
        return min(high, 2**31-1)
        
#leetcode submit region end(Prohibit modification and deletion)
