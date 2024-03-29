#Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]). 
#
# Find the minimum element. 
#
# You may assume no duplicate exists in the array. 
#
# Example 1: 
#
# 
#Input: [3,4,5,1,2] 
#Output: 1
# 
#
# Example 2: 
#
# 
#Input: [4,5,6,7,0,1,2]
#Output: 0
# 
# Related Topics Array Binary Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (high+low)//2
            if nums[mid]<=nums[-1]:
                high = mid -1
            else:
                low = mid +1
        return nums[low]
        
#leetcode submit region end(Prohibit modification and deletion)
