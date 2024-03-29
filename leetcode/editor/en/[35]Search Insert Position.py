#Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. 
#
# You may assume no duplicates in the array. 
#
# Example 1: 
#
# 
#Input: [1,3,5,6], 5
#Output: 2
# 
#
# Example 2: 
#
# 
#Input: [1,3,5,6], 2
#Output: 1
# 
#
# Example 3: 
#
# 
#Input: [1,3,5,6], 7
#Output: 4
# 
#
# Example 4: 
#
# 
#Input: [1,3,5,6], 0
#Output: 0
# 
# Related Topics Array Binary Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low
        
#leetcode submit region end(Prohibit modification and deletion)
