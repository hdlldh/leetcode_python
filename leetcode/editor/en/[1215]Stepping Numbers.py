# A Stepping Number is an integer such that all of its adjacent digits have an a
# bsolute difference of exactly 1. For example, 321 is a Stepping Number while 421
#  is not. 
# 
#  Given two integers low and high, find and return a sorted list of all the Ste
# pping Numbers in the range [low, high] inclusive. 
# 
#  
#  Example 1: 
#  Input: low = 0, high = 21
# Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]
#  
#  
#  Constraints: 
# 
#  
#  0 <= low <= high <= 2 * 10^9 
#  
#  Related Topics Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        
# leetcode submit region end(Prohibit modification and deletion)
