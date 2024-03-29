#Given a non-empty array of integers, return the k most frequent elements. 
#
# Example 1: 
#
# 
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]
# 
#
# 
# Example 2: 
#
# 
#Input: nums = [1], k = 1
#Output: [1] 
# 
#
# Note: 
#
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements. 
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size. 
# 
# Related Topics Hash Table Heap


import collections
import heapq
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, (val, key))
            if len(heap)>k: heapq.heappop(heap)
        ans = []
        while heap:
            val, key = heapq.heappop(heap)
            ans.append(key)
        ans.reverse()
        return ans

        
#leetcode submit region end(Prohibit modification and deletion)
