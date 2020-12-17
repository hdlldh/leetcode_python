# Given an array of integers nums and an integer k. A subarray is called nice if
#  there are k odd numbers on it. 
# 
#  Return the number of nice sub-arrays. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1
# ].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 50000 
#  1 <= nums[i] <= 10^5 
#  1 <= k <= nums.length 
#  
#  Related Topics Two Pointers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l1 = 0
        cnt1 = 0
        l2 = 0
        cnt2 = 0
        ans = 0
        for r, num in enumerate(nums):
            if num % 2:
                cnt1 += 1
                cnt2 += 1
            while cnt1 > k:
                if nums[l1] % 2: cnt1 -= 1
                l1 += 1

            while cnt2 > k - 1:
                if nums[l2] % 2: cnt2 -= 1
                l2 += 1
            ans += l2 - l1
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
