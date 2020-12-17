# Given an array of integers nums and a positive integer k, find whether it's po
# ssible to divide this array into sets of k consecutive numbers 
# Return True if its possible otherwise return False. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,1
# 1].
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3,2,2,1,1], k = 3
# Output: true
#  
# 
#  Example 4: 
# 
#  
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10^5 
#  1 <= nums[i] <= 10^9 
#  1 <= k <= nums.length 
#  
# Note: This question is the same as 846: https://leetcode.com/problems/hand-of-
# straights/ Related Topics Array Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = collections.Counter(nums)
        while count:
            m = min(count)
            v = count[m]
            for i in range(m, m+k):
                if i not in count or count[i] < v: return False
                count[i] -= v
                if count[i] == 0: count.pop(i)
        return True
        
# leetcode submit region end(Prohibit modification and deletion)
