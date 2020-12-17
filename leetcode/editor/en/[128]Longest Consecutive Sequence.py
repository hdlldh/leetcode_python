#Given an unsorted array of integers, find the length of the longest consecutive elements sequence. 
#
# Your algorithm should run in O(n) complexity. 
#
# Example: 
#
# 
#Input: [100, 4, 200, 1, 3, 2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# 
# Related Topics Array Union Find



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hset = set(nums)
        ans = 0
        while hset:
            num = hset.pop()
            size = 1
            left = num
            while left - 1 in hset:
                left -= 1
                hset.remove(left)
                size += 1
            right = num
            while right + 1 in hset:
                right += 1
                hset.remove(right)
                size += 1
            ans = max(ans, size)
        return ans

        
#leetcode submit region end(Prohibit modification and deletion)
