# Given an integer d between 0 and 9, and two positive integers low and high as 
# lower and upper bounds, respectively. Return the number of times that d occurs a
# s a digit in all integers between low and high, including the bounds low and hig
# h.
#  
# 
#  Example 1: 
# 
#  
# Input: d = 1, low = 1, high = 13
# Output: 6
# Explanation: 
# The digit d=1 occurs 6 times in 1,10,11,12,13. Note that the digit d=1 occurs 
# twice in the number 11.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: d = 3, low = 100, high = 250
# Output: 35
# Explanation: 
# The digit d=3 occurs 35 times in 103,113,123,130,131,...,238,239,243.
#  
# 
#  
# 
#  Note: 
# 
#  
#  0 <= d <= 9 
#  1 <= low <= high <= 2×10^8 
#  
#  Related Topics Math Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def digitsCount(self, d, low, high):
        """
        :type d: int
        :type low: int
        :type high: int
        :rtype: int
        """
        
# leetcode submit region end(Prohibit modification and deletion)
