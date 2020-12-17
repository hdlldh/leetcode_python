# Given two lists of closed intervals, each list of intervals is pairwise disjoi
# nt and in sorted order. 
# 
#  Return the intersection of these two interval lists. 
# 
#  (Formally, a closed interval [a, b] (with a <= b) denotes the set of real num
# bers x with a <= x <= b. The intersection of two closed intervals is a set of re
# al numbers that is either empty, or can be represented as a closed interval. For
#  example, the intersection of [1, 3] and [2, 4] is [2, 3].) 
# 
#  
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and
#  not arrays or lists.
#  
# 
#  
# 
#  Note: 
# 
#  
#  0 <= A.length < 1000 
#  0 <= B.length < 1000 
#  0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9 
#  
# 
#  NOTE: input types have been changed on April 15, 2019. Please reset to defaul
# t code definition to get new method signature. 
#  
#  Related Topics Two Pointers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
