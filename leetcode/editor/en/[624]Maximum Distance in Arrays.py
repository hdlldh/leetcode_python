# 
# Given m arrays, and each array is sorted in ascending order. Now you can pick 
# up two integers from two different arrays (each array picks one) and calculate t
# he distance. We define the distance between two integers a and b to be their abs
# olute difference |a-b|. Your task is to find the maximum distance.
#  
# 
#  Example 1: 
#  
# Input: 
# [[1,2,3],
#  [4,5],
#  [1,2,3]]
# Output: 4
# Explanation: 
# One way to reach the maximum distance 4 is to pick 1 in the first or third arr
# ay and pick 5 in the second array.
#  
#  
#  
#  Note: 
#  
#  Each given array will have at least 1 number. There will be at least two non-
# empty arrays. 
#  The total number of the integers in all the m arrays will be in the range of 
# [2, 10000]. 
#  The integers in the m arrays will be in the range of [-10000, 10000]. 
#  
#  Related Topics Array Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        n = len(arrays)
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        ans = 0
        for i in range(1, n):
            ans = max(ans, abs(arrays[i][0]-max_val),abs(arrays[i][-1]-min_val))
            max_val = max(max_val, arrays[i][-1])
            min_val = min(min_val, arrays[i][0])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
