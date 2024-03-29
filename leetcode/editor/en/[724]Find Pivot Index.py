# Given an array of integers nums, write a method that returns the "pivot" index
#  of this array. 
# 
#  We define the pivot index as the index where the sum of the numbers to the le
# ft of the index is equal to the sum of the numbers to the right of the index. 
# 
#  If no such index exists, we should return -1. If there are multiple pivot ind
# exes, you should return the left-most pivot index. 
# 
#  Example 1: 
# 
#  
# Input: 
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation: 
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the su
# m of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: 
# nums = [1, 2, 3]
# Output: -1
# Explanation: 
# There is no index that satisfies the conditions in the problem statement.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The length of nums will be in the range [0, 10000]. 
#  Each element nums[i] will be an integer in the range [-1000, 1000]. 
#  
# 
#  
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N==0: return -1
        if N==1: return 0
        psum = [0]* N
        s = sum(nums)
        psum[0] = nums[0]
        if psum[0] == s- psum[0]+nums[0]: return 0
        for i in range(1,N):
            psum[i] = psum[i-1] + nums[i]
            if psum[i] == s- psum[i]+nums[i]: return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)
