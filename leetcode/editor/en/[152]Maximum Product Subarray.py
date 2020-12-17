#Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product. 
#
# Example 1: 
#
# 
#Input: [2,3,-2,4]
#Output: 6
#Explanation: [2,3] has the largest product 6.
# 
#
# Example 2: 
#
# 
#Input: [-2,0,-1]
#Output: 0
#Explanation: The result cannot be 2, because [-2,-1] is not a subarray. 
# Related Topics Array Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_prod = [0]*n
        min_prod = [0]*n
        max_prod[0] = nums[0]
        min_prod[0] = nums[0]
        ans = nums[0]
        for i in range(1,n):
            max_prod[i] = max(max_prod[i-1]*nums[i], min_prod[i - 1] * nums[i], nums[i])
            min_prod[i] = min(max_prod[i-1]*nums[i], min_prod[i - 1] * nums[i], nums[i])
            ans = max(ans, max_prod[i])
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
