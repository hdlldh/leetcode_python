# Given a sorted array A of unique numbers, find the K-th missing number startin
# g from the leftmost number of the array. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: A = [4,7,9,10], K = 1
# Output: 5
# Explanation: 
# The first missing number is 5.
#  
# 
#  Example 2: 
# 
#  
# Input: A = [4,7,9,10], K = 3
# Output: 8
# Explanation: 
# The missing numbers are [5,6,8,...], hence the third missing number is 8.
#  
# 
#  Example 3: 
# 
#  
# Input: A = [1,2,4], K = 3
# Output: 6
# Explanation: 
# The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 50000 
#  1 <= A[i] <= 1e7 
#  1 <= K <= 1e8 
#  Related Topics Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = low+(high-low)//2
            if self.missing(nums, mid)>=k: high  = mid -1
            else: low = mid +1
        return nums[high] + k -self.missing(nums, high)

    def missing(self, nums, idx):
        return nums[idx] -nums[0]-idx
        
# leetcode submit region end(Prohibit modification and deletion)
