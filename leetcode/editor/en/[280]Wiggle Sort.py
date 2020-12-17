#Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3].... 
#
# Example: 
#
# 
#Input: nums = [3,5,2,1,6,4]
#Output: One possible answer is [3,5,1,6,2,4] 
# Related Topics Array Sort



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        if n <= 2: return nums
        i = 1
        j = 2
        while j<n:
            nums[i], nums[j] = nums[j], nums[i]
            i+=2
            j+=2
#leetcode submit region end(Prohibit modification and deletion)
