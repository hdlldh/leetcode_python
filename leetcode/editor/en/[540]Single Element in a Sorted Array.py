#You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once. 
#
# 
#
# Example 1: 
#
# 
#Input: [1,1,2,3,3,4,4,8,8]
#Output: 2
# 
#
# Example 2: 
#
# 
#Input: [3,3,7,7,10,11,11]
#Output: 10
# 
#
# 
#
# Note: Your solution should run in O(log n) time and O(1) space. 
#



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid == n - 1: return nums[n - 1]
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]

#leetcode submit region end(Prohibit modification and deletion)
