#Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one. 
#
# Example 1: 
#
# 
#Input: [1,3,4,2,2]
#Output: 2
# 
#
# Example 2: 
#
# 
#Input: [3,1,3,4,2]
#Output: 3 
#
# Note: 
#
# 
# You must not modify the array (assume the array is read only). 
# You must use only constant, O(1) extra space. 
# Your runtime complexity should be less than O(n2). 
# There is only one duplicate number in the array, but it could be repeated more than once. 
# 
# Related Topics Array Two Pointers Binary Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 1
        high = n
        while low<=high:
            mid = low + (high-low)//2
            cnt = 0
            for num in nums:
                if num<=mid: cnt+=1
            if cnt <= mid: low = mid +1
            else: high = mid -1
        return low

#leetcode submit region end(Prohibit modification and deletion)
