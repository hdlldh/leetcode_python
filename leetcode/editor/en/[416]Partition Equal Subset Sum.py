# Given a non-empty array containing only positive integers, find if the array c
# an be partitioned into two subsets such that the sum of elements in both subsets
#  is equal. 
# 
#  Note: 
# 
#  
#  Each of the array element will not exceed 100. 
#  The array size will not exceed 200. 
#  
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
#  
# 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sm = sum(nums)
        n = len(nums)
        if sm%2!=0: return False
        target = sm//2
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            if num >target: return False
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[target]
# leetcode submit region end(Prohibit modification and deletion)
