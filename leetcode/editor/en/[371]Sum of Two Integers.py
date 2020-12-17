#Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -. 
#
# 
# Example 1: 
#
# 
#Input: a = 1, b = 2
#Output: 3
# 
#
# 
# Example 2: 
#
# 
#Input: a = -2, b = 3
#Output: 1
# 
# 
# 
# Related Topics Bit Manipulation



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF;
        while b:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)

        
#leetcode submit region end(Prohibit modification and deletion)
