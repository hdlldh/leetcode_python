# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements ap
# pear twice and others appear once. 
# 
#  Find all the elements that appear twice in this array. 
# 
#  Could you do it without extra space and in O(n) runtime? 
#  
#  Example: 
#  
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [2,3]
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i = 0
        ans = []
        while i<n:
            if nums[i] != nums[nums[i]-1]:
                j = nums[i] -1
                nums[i], nums[j] = nums[j], nums[i]
                continue
            i += 1
        for i in range(n):
            if nums[i] != i+1: ans.append(nums[i])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
