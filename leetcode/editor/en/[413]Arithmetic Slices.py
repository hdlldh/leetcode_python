# A sequence of number is called arithmetic if it consists of at least three ele
# ments and if the difference between any two consecutive elements is the same. 
# 
#  For example, these are arithmetic sequence: 
#  1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9 
# 
#  The following sequence is not arithmetic. 1, 1, 2, 5, 7 
#  
# 
#  A zero-indexed array A consisting of N numbers is given. A slice of that arra
# y is any pair of integers (P, Q) such that 0 <= P < Q < N. 
# 
#  A slice (P, Q) of array A is called arithmetic if the sequence: 
#  A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means 
# that P + 1 < Q. 
# 
#  The function should return the number of arithmetic slices in the array A. 
#  
# 
#  Example:
#  
# A = [1, 2, 3, 4]
# 
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4]
#  itself.
#  Related Topics Math Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        ans = 0
        dp = [0] *n
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
            ans += dp[i]
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)
