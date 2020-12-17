#Given an integer array sorted in ascending order, write a function to search ta
#rget in nums. If target exists, then return its index, otherwise return -1. Howe
#ver, the array size is unknown to you. You may only access the array using an Ar
#rayReader interface, where ArrayReader.get(k) returns the element of the array a
#t index k (0-indexed). 
#
# You may assume all integers in the array are less than 10000, and if you acces
#s the array out of bounds, ArrayReader.get will return 2147483647. 
#
# 
#
# Example 1: 
#
# 
#Input: array = [-1,0,3,5,9,12], target = 9
#Output: 4
#Explanation: 9 exists in nums and its index is 4
# 
#
# Example 2: 
#
# 
#Input: array = [-1,0,3,5,9,12], target = 2
#Output: -1
#Explanation: 2 does not exist in nums so return -1 
#
# 
#
# Note: 
#
# 
# You may assume that all elements in the array are unique. 
# The value of each element in the array will be in the range [-9999, 9999]. 
# 
# Related Topics Binary Search




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        low = 0
        high = 10000
        invalid = 2147483647
        while low<=high:
            mid = low + (high-low)//2
            t = reader.get(mid)
            if t==invalid or t>target: high = mid -1
            elif t<target: low = mid +1
            else: return mid
        return -1
        
#leetcode submit region end(Prohibit modification and deletion)
