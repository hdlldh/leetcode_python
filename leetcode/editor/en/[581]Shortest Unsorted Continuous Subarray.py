# Given an integer array, you need to find one continuous subarray that if you o
# nly sort this subarray in ascending order, then the whole array will be sorted i
# n ascending order, too. 
# 
#  You need to find the shortest such subarray and output its length. 
# 
#  Example 1: 
#  
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the 
# whole array sorted in ascending order.
#  
#  
# 
#  Note: 
#  
#  Then length of the input array is in range [1, 10,000]. 
#  The input array may contain duplicates, so ascending order here means <=. 
#  
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
# leetcode submit region end(Prohibit modification and deletion)
