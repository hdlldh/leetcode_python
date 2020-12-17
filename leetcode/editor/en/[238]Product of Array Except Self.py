#Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i]. 
#
# Example: 
#
# 
#Input:  [1,2,3,4]
#Output: [24,12,8,6]
# 
#
# Note: Please solve it without division and in O(n). 
#
# Follow up: 
#Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.) 
# Related Topics Array



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l2r = [1]*n
        r2l = [1]*n
        for i in range(1,n):
            l2r[i] = l2r[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            r2l[i] = r2l[i+1] * nums[i+1]

        print(l2r, r2l)
        for i in range(n):
            l2r[i] = l2r[i] * r2l[i]
        return l2r
        
#leetcode submit region end(Prohibit modification and deletion)
