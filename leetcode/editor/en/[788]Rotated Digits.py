# X is a good number if after rotating each digit individually by 180 degrees, w
# e get a valid number that is different from X. Each digit must be rotated - we c
# annot choose to leave it alone. 
# 
#  A number is valid if each digit remains a digit after rotation. 0, 1, and 8 r
# otate to themselves; 2 and 5 rotate to each other (on this case they are rotated
#  in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate 
# to each other, and the rest of the numbers do not rotate to any other number and
#  become invalid. 
# 
#  Now given a positive number N, how many numbers X from 1 to N are good? 
# 
#  
# Example:
# Input: 10
# Output: 4
# Explanation: 
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rot
# ating.
#  
# 
#  Note: 
# 
#  
#  N will be in range [1, 10000]. 
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
# leetcode submit region end(Prohibit modification and deletion)
