# Given an integer number n, return the difference between the product of its di
# gits and the sum of its digits.
#  
#  Example 1: 
# 
#  
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
#  
# 
#  Example 2: 
# 
#  
# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10^5 
#  
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod = 1
        s = 0
        while n:
            prod *= n%10
            s += n%10
            n = n//10
        return prod -s
        
# leetcode submit region end(Prohibit modification and deletion)
