# 
# Given an unsorted array of integers, find the length of longest continuous inc
# reasing subsequence (subarray).
#  
# 
#  Example 1: 
#  
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its len
# gth is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous
#  one where 5 and 7 are separated by 4. 
#  
#  
# 
#  Example 2: 
#  
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length 
# is 1. 
#  
#  
# 
#  Note:
# Length of the array will not exceed 10,000.
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N==0: return 0
        dp =[1]*N
        for i in range(1,N):
            if nums[i]>nums[i-1]:
                dp[i] = dp[i-1]+1
        return max(dp)
# leetcode submit region end(Prohibit modification and deletion)
