# (This problem is an interactive problem.) 
# 
#  You may recall that an array A is a mountain array if and only if: 
# 
#  
#  A.length >= 3 
#  There exists some i with 0 < i < A.length - 1 such that:
#  
#  A[0] < A[1] < ... A[i-1] < A[i] 
#  A[i] > A[i+1] > ... > A[A.length - 1] 
#  
#  
#  
# 
#  Given a mountain array mountainArr, return the minimum index such that mounta
# inArr.get(index) == target. If such an index doesn't exist, return -1. 
# 
#  You can't access the mountain array directly. You may only access the array u
# sing a MountainArray interface: 
# 
#  
#  MountainArray.get(k) returns the element of the array at index k (0-indexed).
#  
#  MountainArray.length() returns the length of the array. 
#  
# 
#  Submissions making more than 100 calls to MountainArray.get will be judged Wr
# ong Answer. Also, any solutions that attempt to circumvent the judge will result
#  in disqualification. 
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum
#  index, which is 2. 
# 
#  Example 2: 
# 
#  
# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= mountain_arr.length() <= 10000 
#  0 <= target <= 10^9 
#  0 <= mountain_arr.get(index) <= 10^9 
#  
#  Related Topics Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountain_arr.length()
        if n==0: return -1
        low = 1
        high = n-2
        while low <= high:
            mid = low + (high-low)//2
            left = mountain_arr.get(mid-1)
            curr = mountain_arr.get(mid)
            right = mountain_arr.get(mid+1)
            if  left<curr<right: low = mid +1
            elif left>curr>right: high = mid -1
            else: break

        low = 0
        high = mid
        while low <= high:
            mid1 = low + (high-low)//2
            curr = mountain_arr.get(mid1)
            if curr > target: high = mid1 -1
            elif curr < target: low = mid1 + 1
            else: return mid1

        low = mid
        high = n-1
        while low <= high:
            mid1 = low + (high-low)//2
            curr = mountain_arr.get(mid1)
            if curr < target: high = mid1 -1
            elif curr > target: low = mid1 + 1
            else: return mid1
        return -1

# leetcode submit region end(Prohibit modification and deletion)
