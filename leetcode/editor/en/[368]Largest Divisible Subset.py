#Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: 
#
# Si % Sj = 0 or Sj % Si = 0. 
#
# If there are multiple solutions, return any subset is fine. 
#
# Example 1: 
#
# 
# 
#Input: [1,2,3]
#Output: [1,2] (of course, [1,3] will also be ok)
# 
#
# 
# Example 2: 
#
# 
#Input: [1,2,4,8]
#Output: [1,2,4,8]
# 
# 
# Related Topics Math Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
#leetcode submit region end(Prohibit modification and deletion)
