#Given an array A of non-negative integers, return the maximum sum of elements i
#n two non-overlapping (contiguous) subarrays, which have lengths L and M. (For c
#larification, the L-length subarray could occur before or after the M-length sub
#array.) 
#
# Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) 
#+ (A[j] + A[j+1] + ... + A[j+M-1]) and either: 
#
# 
# 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or 
# 0 <= j < j + M - 1 < i < i + L - 1 < A.length. 
# 
#
# 
#
# 
# 
#
# 
# Example 1: 
#
# 
#Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
#Output: 20
#Explanation: One choice of subarrays is [9] with length 1, and [6,5] with lengt
#h 2.
# 
#
# 
# Example 2: 
#
# 
#Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
#Output: 29
#Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with l
#ength 2.
# 
#
# 
# Example 3: 
#
# 
#Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
#Output: 31
#Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with
# length 3.
# 
#
# 
#
# Note: 
#
# 
# L >= 1 
# M >= 1 
# L + M <= A.length <= 1000 
# 0 <= A[i] <= 1000 
# 
# 
# 
# 
# Related Topics Array




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        n = len(A)
        psum = [0]*n
        psum[0] = A[0]
        for i in range(1,n):
            psum[i] = psum[i-1]+A[i]
        Lmax = sum(A[:L])
        Mmax = sum(A[:M])
        ans = 0
        for i in range(n):
            if i>=L and i+M-1<n:
                ans = max(ans, Lmax + psum[i+M-1]-psum[i-1])
            if i>=M and i+L-1<n:
                ans = max(ans, Mmax + psum[i + L - 1] - psum[i - 1])
            if i>=L:
                Lmax = max(Lmax, psum[i]-psum[i-L])
            if i>=M:
                Mmax = max(Mmax, psum[i]-psum[i-M])
        return ans

        
#leetcode submit region end(Prohibit modification and deletion)
