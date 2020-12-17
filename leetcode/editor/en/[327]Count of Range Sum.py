#Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive. 
#Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive. 
#
# Note: 
#A naive algorithm of O(n2) is trivial. You MUST do better than that. 
#
# Example: 
#
# 
#Input: nums = [-2,5,-1], lower = -2, upper = 2,
#Output: 3 
#Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
# Related Topics Binary Search Divide and Conquer Sort Binary Indexed Tree Segment Tree


import bisect
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(nums)
        if n==0: return 0
        treeKey = [0]
        treeCnt = {}
        treeCnt[0] = 1
        sumi = 0
        ans = 0
        for i in range(n):
            sumi += nums[i]
            left = bisect.bisect_left(treeKey, sumi-upper)
            right = bisect.bisect_right(treeKey, sumi-lower)
            for j in range(left, right):
                ans += treeCnt[treeKey[j]]
            left = bisect.bisect_left(treeKey, sumi)
            if left < len(treeKey) and sumi == treeKey[left]:
                treeCnt[sumi] += 1
            else:
                treeKey.insert(left, sumi)
                treeCnt[sumi] = 1
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
