#Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value. 
#
# Your algorithm's runtime complexity must be in the order of O(log n). 
#
# If the target is not found in the array, return [-1, -1]. 
#
# Example 1: 
#
# 
#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4] 
#
# Example 2: 
#
# 
#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1] 
# Related Topics Array Binary Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target: high = mid - 1
            else: low = mid + 1
        leftmost = low if low < n and nums[low] == target else -1

        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target: high = mid - 1
            else: low = mid + 1
        rightmost = high if high >= 0 and nums[high] == target else -1
        return [leftmost, rightmost]
#leetcode submit region end(Prohibit modification and deletion)
