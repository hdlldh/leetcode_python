# In a given array nums of positive integers, find three non-overlapping subarra
# ys with maximum sum. 
# 
#  Each subarray will be of size k, and we want to maximize the sum of all 3*k e
# ntries. 
# 
#  Return the result as a list of indices representing the starting position of 
# each interval (0-indexed). If there are multiple answers, return the lexicograph
# ically smallest one. 
# 
#  Example: 
# 
#  
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indic
# es [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicogra
# phically larger.
#  
# 
#  
# 
#  Note: 
# 
#  
#  nums.length will be between 1 and 20000. 
#  nums[i] will be between 1 and 65535. 
#  k will be between 1 and floor(nums.length / 3). 
#  
# 
#  
#  Related Topics Array Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        psum =[0] * (n+1)
        for i, num in enumerate(nums):
            psum[i+1] = psum[i] + num

        left = [0] * n
        #left[0] = 0
        total = psum[k] - psum[0]
        for i in range(1, n-k+1):
            if psum[i+k] - psum[i] > total:
                left[i] = i
                total = psum[i+k] - psum[i]
            else: left[i] = left[i-1]

        right = [n-k] * n
        #right[n-k] = n-k
        total = psum[n] - psum[n-k]
        for i in range(n-k-1, -1, -1):
            if psum[i+k] - psum[i] >= total:
                right[i] = i
                total = psum[i+k] - psum[i]
            else: right[i] = right[i+1]

        mx = 0
        ans = []
        for i in range(k, n-2*k+1):
            l = left[i-k]
            r = right[i+k]
            x = psum[l+k] - psum[l] + psum[i+k] - psum[i] + psum[r+k] - psum[r]
            if x > mx:
                ans = [l, i, r]
                mx = x
        return ans

# leetcode submit region end(Prohibit modification and deletion)
