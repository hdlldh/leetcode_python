# Given a positive integer a, find the smallest positive integer b whose multipl
# ication of each digit equals to a. 
# 
#  
# If there is no answer or the answer is not fit in 32-bit signed integer, then 
# return 0. 
# 
#  
# Example 1 
# Input:
#  48 
# Output:
#  68 
#  
# 
#  
# Example 2 
# Input: 
#  15 
# 
# Output:
#  35 
#  Related Topics Math Recursion


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        ans = float('inf')
        if a < 10: return a
        ans = 0
        mul = 1
        for i in range(9, 1, -1):
            while a%i==0:
                a = a//i
                ans += mul * i
                mul *=10

        if a ==1 and ans< 0x7fffffff: return ans
        return 0

# leetcode submit region end(Prohibit modification and deletion)
