#Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution. 
#
# Example: 
#
# 
#Given array nums = [-1, 2, 1, -4], and target = 1.
#
#The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# Related Topics Array Two Pointers



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = float('inf')
        n = len(nums)
        i = 0
        while i<n:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j = i+1
            k = n-1
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                elif s > target:
                    if s-target < abs(ans-target):
                        ans = s
                    k-=1
                else:
                    if target - s < abs(ans - target):
                        ans = s
                    j+=1
            i+=1
        return ans
#leetcode submit region end(Prohibit modification and deletion)
