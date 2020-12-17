#Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal. 
#
# 
#
# Example 1: 
#
# 
#Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
#Output: True
#Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# 
#
# 
#
# Note: 
#
# 
# 1 <= k <= len(nums) <= 16. 
# 0 < nums[i] < 10000. 
# 
# Related Topics Dynamic Programming Recursion



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        sums = sum(nums)
        if sums%k!=0: return False
        target = sums//k
        nums.sort()
        if nums[-1]>target: return False
        if k==1: return True
        checker = [0]*k

        def dfs(nums, k, start, target, checker):
            if start <0:
                for num in checker:
                    if num!=target: return False
                return True
            for i in range(k):
                if nums[start]+checker[i]>target: continue
                checker[i] += nums[start]
                if dfs(nums, k, start-1, target, checker): return True
                checker[i] -= nums[start]
            return False

        return dfs(nums, k, len(nums)-1, target, checker)




#leetcode submit region end(Prohibit modification and deletion)
