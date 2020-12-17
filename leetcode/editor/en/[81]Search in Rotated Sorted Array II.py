#Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]). 
#
# You are given a target value to search. If found in the array return true, otherwise return false. 
#
# Example 1: 
#
# 
#Input: nums = [2,5,6,0,0,1,2], target = 0
#Output: true
# 
#
# Example 2: 
#
# 
#Input: nums = [2,5,6,0,0,1,2], target = 3
#Output: false 
#
# Follow up: 
#
# 
# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates. 
# Would this affect the run-time complexity? How and why? 
# 
# Related Topics Array Binary Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        if n == 0: return False
        loc = self.findMin(nums)
        if target <= nums[-1]:
            return self.biSearch(nums, loc, n - 1, target)
        else:
            return self.biSearch(nums, 0, loc - 1, target)

    def findMin(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        while low<high and nums[low]==nums[high]:low+=1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] <= nums[-1]:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def biSearch(self, nums, start, end, target):
        low = start
        high = end
        while low<=high:
            mid = low + (high - low)//2
            if nums[mid]> target:
                high = mid-1
            elif nums[mid] < target:
                low = mid +1
            else:
                return True
        return False
        
#leetcode submit region end(Prohibit modification and deletion)
