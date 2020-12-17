# 
# Given a circular array (the next element of the last element is the first elem
# ent of the array), print the Next Greater Number for every element. The Next Gre
# ater Number of a number x is the first greater number to its traversing-order ne
# xt in the array, which means you could search circularly to find its next greate
# r number. If it doesn't exist, output -1 for this number.
#  
# 
#  Example 1: 
#  
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find n
# ext greater number; The second 1's next greater number needs to search circularl
# y, which is also 2.
#  
#  
# 
#  Note:
# The length of given array won't exceed 10000.
#  Related Topics Stack


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [-1] * n
        for i in xrange(n):
            for j in xrange(1,n):
                if nums[(i+j)%n] > nums[i]:
                    ans[i] = nums[(i+j)%n]
                    break
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
