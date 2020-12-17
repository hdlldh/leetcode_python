# 
# Given a binary array, find the maximum number of consecutive 1s in this array 
# if you can flip at most one 0.
#  
# 
#  Example 1: 
#  
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of consecutiv
# e 1s.
#     After flipping, the maximum number of consecutive 1s is 4.
#  
#  
# 
#  Note:
#  
#  The input array will only contain 0 and 1. 
#  The length of input array is a positive integer and will not exceed 10,000 
#  
#  
# 
#  Follow up: 
# What if the input numbers come in one by one as an infinite stream? In other w
# ords, you can't store all numbers coming from the stream as it's too large to ho
# ld in memory. Could you solve it efficiently?
#  Related Topics Two Pointers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 1
        n = len(nums)
        ans = 0
        left = [0] * n
        for i in range(1, n):
            if nums[i - 1] == 1:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 0

        right = [0] * n
        for i in range(n - 2, -1, -1):
            if nums[i + 1] == 1:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 0

        for i in range(n):
            ans = max(ans, left[i] + right[i] + 1)
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
