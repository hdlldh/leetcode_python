#Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array. 
#
# Formally the function should: 
#
# Return true if there exists i, j, k 
#such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false. 
#
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity. 
#
# 
# Example 1: 
#
# 
#Input: [1,2,3,4,5]
#Output: true
# 
#
# 
# Example 2: 
#
# 
#Input: [5,4,3,2,1]
#Output: false
# 
# 
#



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for num in nums:
            if num<=first: first = num
            elif num <= second: second = num
            else: return True
        return False
#leetcode submit region end(Prohibit modification and deletion)
