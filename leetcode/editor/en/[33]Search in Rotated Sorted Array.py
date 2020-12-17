#Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]). 
#
# You are given a target value to search. If found in the array return its index, otherwise return -1. 
#
# You may assume no duplicate exists in the array. 
#
# Your algorithm's runtime complexity must be in the order of O(log n). 
#
# Example 1: 
#
# 
#Input: nums = [4,5,6,7,0,1,2], target = 0
#Output: 4
# 
#
# Example 2: 
#
# 
#Input: nums = [4,5,6,7,0,1,2], target = 3
#Output: -1 
# Related Topics Array Binary Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n==0: return -1
        loc = self.findMin(nums)
        if target<= nums[-1]:
            return self.biSearch(nums, loc, n-1, target)
        else:
            return self.biSearch(nums, 0, loc-1, target)

    def findMin(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
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
                return mid
        return -1

        
#leetcode submit region end(Prohibit modification and deletion)
