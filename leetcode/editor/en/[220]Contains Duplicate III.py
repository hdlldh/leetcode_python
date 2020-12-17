#Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k. 
#
# 
# Example 1: 
#
# 
#Input: nums = [1,2,3,1], k = 3, t = 0
#Output: true
# 
#
# 
# Example 2: 
#
# 
#Input: nums = [1,0,1,1], k = 1, t = 2
#Output: true
# 
#
# 
# Example 3: 
#
# 
#Input: nums = [1,5,9,1,5,9], k = 2, t = 3
#Output: false
# 
# 
# 
# Related Topics Sort Ordered Map


import collections
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0: return False
        window = collections.OrderedDict()
        for num in nums:
            bucketId = num if t == 0 else num // t
            if len(window) > k: window.popitem(False)
            for m in (window.get(bucketId - 1), window.get(bucketId), window.get(bucketId + 1)):
                if m is not None and abs(m - num) <= t: return True
            window[bucketId] = num
        return False
        
#leetcode submit region end(Prohibit modification and deletion)
