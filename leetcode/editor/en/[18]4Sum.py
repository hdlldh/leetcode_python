#Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target. 
#
# Note: 
#
# The solution set must not contain duplicate quadruplets. 
#
# Example: 
#
# 
#Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
#A solution set is:
#[
#  [-1,  0, 0, 1],
#  [-2, -1, 1, 2],
#  [-2,  0, 0, 2]
#]
# 
# Related Topics Array Hash Table Two Pointers



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        n = len(nums)
        i = 0
        while i<n:
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j = i+1
            while j<n:
                if j!=i+1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                k = j+1
                l = n-1
                while k<l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s==target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k+=1
                        while k<l and nums[k]==nums[k-1]: k+=1
                    elif s>target: l-=1
                    else: k+=1
                j+=1
            i+=1
        return ans

        
#leetcode submit region end(Prohibit modification and deletion)
