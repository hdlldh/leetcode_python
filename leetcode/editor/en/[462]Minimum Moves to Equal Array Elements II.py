# Given a non-empty integer array, find the minimum number of moves required to 
# make all array elements equal, where a move is incrementing a selected element b
# y 1 or decrementing a selected element by 1. 
# 
#  You may assume the array's length is at most 10,000. 
# 
#  Example:
#  
# Input:
# [1,2,3]
# 
# Output:
# 2
# 
# Explanation:
# Only two moves are needed (remember each move increments or decrements one ele
# ment):
# 
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
#  
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        i = 0
        j = n-1
        ans = 0
        while i < j:
            ans += nums[j] - nums[i]
            i += 1
            j -= 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
