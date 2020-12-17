# 
# Given an array with n integers, you need to find if there are triplets (i, j, 
# k) which satisfies following conditions:
#  
#  0 < i, i + 1 < j, j + 1 < k < n - 1 
#  Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1
# ) should be equal. 
#  
# where we define that subarray (L, R) represents a slice of the original array 
# starting from the element indexed L to the element indexed R.
#  
# 
#  Example: 
#  
# Input: [1,2,1,2,1,2,1]
# Output: True
# Explanation:
# i = 1, j = 3, k = 5. 
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1
#  
#  
# 
# Note:
#  
#  1 <= n <= 2000. 
#  Elements in the given array will be in range [-1,000,000, 1,000,000]. 
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        if N<7: return False
        psum = [0] * N
        psum[0] = nums[0]
        for i in range(1, N):
            psum[i] = psum[i-1] + nums[i]
        for j in range(3, N-2):
            mem = set()
            for i in range(1, j-1):
                if psum[i-1] == psum[j-1]-psum[i]:
                    mem.add(psum[i-1])
            for k in range(j+2, N-1):
                if psum[k-1]-psum[j] == psum[N-1]- psum[k] and psum[k-1]-psum[j] in mem:return True

        return False


        
# leetcode submit region end(Prohibit modification and deletion)
