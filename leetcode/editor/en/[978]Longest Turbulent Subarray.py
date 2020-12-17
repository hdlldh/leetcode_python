# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if
# : 
# 
#  
#  For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even
# ; 
#  OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is
#  odd. 
#  
# 
#  That is, the subarray is turbulent if the comparison sign flips between each 
# adjacent pair of elements in the subarray. 
# 
#  Return the length of a maximum size turbulent subarray of A. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [4,8,12,16]
# Output: 2
#  
# 
#  
#  Example 3: 
# 
#  
# Input: [100]
# Output: 1
#  
#  
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 40000 
#  0 <= A[i] <= 10^9 
#  Related Topics Array Dynamic Programming Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dn = [1] * n
        up = [1] * n
        for i in range(1, n):
            if A[i] > A[i - 1]:
                up[i] = max(up[i], dn[i - 1] + 1)
            elif A[i] < A[i - 1]:
                dn[i] = max(dn[i], up[i - 1] + 1)
        return max(up + dn)
# leetcode submit region end(Prohibit modification and deletion)
