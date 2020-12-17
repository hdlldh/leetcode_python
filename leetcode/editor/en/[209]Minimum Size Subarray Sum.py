#Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead. 
#
# Example: 
#
# 
#Input: s = 7, nums = [2,3,1,2,4,3]
#Output: 2
#Explanation: the subarray [4,3] has the minimal length under the problem constraint. 
#
# Follow up: 
#
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
# Related Topics Array Two Pointers Binary Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        csum = [0] * (n+1)
        for i in range(n):
            csum[i+1] = csum[i] + nums[i]
        if csum[-1] < s: return 0
        minLen = float('inf')
        for i in range(n):
            if csum[-1] - csum[i] < s: continue
            low = i + 1
            high = n
            while low <= high:
                mid = (low + high) // 2
                if (csum[mid] - csum[i]) >= s:
                    high = mid - 1
                else:
                    low = mid + 1
            minLen = min(minLen, low - i)

        return minLen

#leetcode submit region end(Prohibit modification and deletion)
