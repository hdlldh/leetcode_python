#Given an array of non-negative integers, you are initially positioned at the first index of the array. 
#
# Each element in the array represents your maximum jump length at that position. 
#
# Your goal is to reach the last index in the minimum number of jumps. 
#
# Example: 
#
# 
#Input: [2,3,1,1,4]
#Output: 2
#Explanation: The minimum number of jumps to reach the last index is 2.
#    Jump 1 step from index 0 to 1, then 3 steps to the last index. 
#
# Note: 
#
# You can assume that you can always reach the last index. 
# Related Topics Array Greedy



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1: return 0
        last = 0
        cur = 0
        ans = 0
        for i in range(n-1):
            cur = max(cur, nums[i]+i)
            if i == last:
               last = cur
               ans += 1
               if last>=n-1: break
        return ans

        
#leetcode submit region end(Prohibit modification and deletion)
