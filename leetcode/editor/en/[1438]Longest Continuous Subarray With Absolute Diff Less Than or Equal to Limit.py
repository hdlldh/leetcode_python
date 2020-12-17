# Given an array of integers nums and an integer limit, return the size of the l
# ongest non-empty subarray such that the absolute difference between any two elem
# ents of this subarray is less than or equal to limit. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute 
# diff is |2-7| = 5 <= 5.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10^5 
#  1 <= nums[i] <= 10^9 
#  0 <= limit <= 10^9 
#  
#  Related Topics Array Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        inc_q = collections.deque()
        dec_q = collections.deque()
        l = 0
        ans = 0
        for r, num in enumerate(nums):
            while inc_q and num < inc_q[-1]:
                inc_q.pop()
            inc_q.append(num)
            while dec_q and num > dec_q[-1]:
                dec_q.pop()
            dec_q.append(num)
            while dec_q[0] - inc_q[0]>limit:
                if nums[l] == inc_q[0]: inc_q.popleft()
                if nums[l] == dec_q[0]: dec_q.popleft()
                l += 1
            ans = max(ans, r-l+1)
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
