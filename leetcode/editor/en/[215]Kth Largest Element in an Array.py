#Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element. 
#
# Example 1: 
#
# 
#Input: [3,2,1,5,6,4] and k = 2
#Output: 5
# 
#
# Example 2: 
#
# 
#Input: [3,2,3,1,2,4,5,5,6] and k = 4
#Output: 4 
#
# Note: 
#You may assume k is always valid, 1 ≤ k ≤ array's length. 
# Related Topics Divide and Conquer Heap



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.partition(nums, k - 1, 0, len(nums) - 1)

    def partition(self, nums, k, start, end):
        if start >= end: return nums[k]
        left = start
        right = end
        pivot = nums[left + (right - left) // 2]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k >= left: return self.partition(nums, k, left, end)
        if k <= right: return self.partition(nums, k, start, right)
        return nums[k]



        
#leetcode submit region end(Prohibit modification and deletion)
