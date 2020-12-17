# 
# Given an array consisting of n integers, find the contiguous subarray whose le
# ngth is greater than or equal to k that has the maximum average value. And you n
# eed to output the maximum average value.
#  
# 
# 
#  Example 1: 
#  
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.
#  
#  
# 
# 
#  Note: 
#  
#  1 <= k <= n <= 10,000. 
#  Elements of the given array will be in range [-10,000, 10,000]. 
#  The answer with the calculation error less than 10-5 will be accepted. 
#  
#  Related Topics Array Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        low = min(nums)
        high = max(nums)
        n = len(nums)
        sums = [0] * (n+1)
        while high -low > 10**(-5):
            mid = low + (high-low)*0.5
            minSum = 0
            check = False
            for i in range(1, n+1):
                sums[i] = sums[i-1]+nums[i-1]-mid
                if i>=k:
                    minSum = min(minSum, sums[i - k])
                    if sums[i] - minSum >= 0:
                        check = True
                        break
            if check: low = mid
            else: high = mid
        return low

        
# leetcode submit region end(Prohibit modification and deletion)
