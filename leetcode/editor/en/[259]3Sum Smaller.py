#Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target. 
#
# Example: 
#
# 
#Input: nums = [-2,0,1,3], and target = 2
#Output: 2 
#Explanation: Because there are two triplets which sums are less than 2:
#             [-2,0,1]
#             [-2,0,3]
# 
#
# Follow up: Could you solve it in O(n2) runtime? 
# Related Topics Array Two Pointers



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n <3: return 0
        cnt = 0
        nums.sort()
        for i in range(0, n-2):
            rest = target- nums[i]
            k = n-1
            for j in range(i+1, n-1):
                while k>j and nums[j]+nums[k]>=rest:
                    k -= 1
                if k>j: cnt += k-j
        return cnt

        
#leetcode submit region end(Prohibit modification and deletion)
