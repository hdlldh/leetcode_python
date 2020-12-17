# Your are given an array of positive integers nums. 
#  Count and print the number of (contiguous) subarrays where the product of all
#  the elements in the subarray is less than k. 
# 
#  Example 1: 
#  
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [
# 2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly les
# s than k.
#  
#  
# 
#  Note:
#  0 < nums.length <= 50000. 
#  0 < nums[i] < 1000. 
#  0 <= k < 10^6. 
#  Related Topics Array Two Pointers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prod = 1
        left = 0
        ans = 0
        for i, num in enumerate(nums):
            prod *= num
            while left <=i and prod >= k:
                prod = prod // nums[left]
                left += 1
            ans += i - left +1
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
