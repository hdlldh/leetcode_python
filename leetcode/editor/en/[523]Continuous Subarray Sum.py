#Given a list of non-negative numbers and a target integer k, write a function t
#o check if the array has a continuous subarray of size at least 2 that sums up t
#o a multiple of k, that is, sums up to n*k where n is also an integer. 
#
# 
#
# Example 1: 
#
# 
#Input: [23, 2, 4, 6, 7],  k=6
#Output: True
#Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6
#.
# 
#
# Example 2: 
#
# 
#Input: [23, 2, 6, 4, 7],  k=6
#Output: True
#Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and s
#ums up to 42.
# 
#
# 
#
# Note: 
#
# 
# The length of the array won't exceed 10,000. 
# You may assume the sum of all the numbers is in the range of a signed 32-bit i
#nteger. 
# 
# Related Topics Math Dynamic Programming




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        psum = 0
        mem = {}
        mem[0] = -1
        for i, num in enumerate(nums):
            psum += num
            t = psum if k==0 else psum % k
            if t in mem:
                if i - mem[t] > 1:return True
            else:
                mem[t] = i
        return False

    def checkSubarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k==0:
            cnt = 0
            for num in nums:
                if num==0:
                    cnt+=1
                    if cnt>=2: return True
                else: cnt = 0
            return False
        mem = {0:-1}
        psum = 0
        for i, num in enumerate(nums):
            psum+=num
            r = psum % k
            if r in mem and i-mem[r]>=2: return True
            if r not in mem: mem[r] = i
        return False
        
#leetcode submit region end(Prohibit modification and deletion)
