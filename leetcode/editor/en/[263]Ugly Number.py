#Write a program to check whether a given number is an ugly number. 
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example 1: 
#
# 
#Input: 6
#Output: true
#Explanation: 6 = 2 × 3 
#
# Example 2: 
#
# 
#Input: 8
#Output: true
#Explanation: 8 = 2 × 2 × 2
# 
#
# Example 3: 
#
# 
#Input: 14
#Output: false 
#Explanation: 14 is not ugly since it includes another prime factor 7.
# 
#
# Note: 
#
# 
# 1 is typically treated as an ugly number. 
# Input is within the 32-bit signed integer range: [−231, 231 − 1]. 
# Related Topics Math



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for p in [2,3,5]:
            while num>0 and num%p==0:
                num = num//p
        return num==1
        
#leetcode submit region end(Prohibit modification and deletion)
