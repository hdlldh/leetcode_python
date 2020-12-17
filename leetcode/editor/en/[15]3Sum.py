#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero. 
#
# Note: 
#
# The solution set must not contain duplicate triplets. 
#
# Example: 
#
# 
#Given array nums = [-1, 0, 1, 2, -1, -4],
#
#A solution set is:
#[
#  [-1, 0, 1],
#  [-1, -1, 2]
#]
# 
# Related Topics Array Two Pointers



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        i = 0
        ans = []
        while i<n:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j = i+1
            k = n-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s==0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j<k and nums[j] == nums[j-1]: j+=1
                elif s>0: k-=1
                else: j += 1
            i+=1
        return ans

        
#leetcode submit region end(Prohibit modification and deletion)
