# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, 
# k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero. 
# 
#  To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ 
# N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guar
# anteed to be at most 231 - 1. 
# 
#  Example: 
# 
#  
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# Output:
# 2
# 
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#  
# 
#  
#  Related Topics Hash Table Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sum1 = collections.defaultdict(int)
        sum2 = collections.defaultdict(int)
        n = len(A)
        for i in range(n):
            for j in range(n):
                sum1[A[i]+B[j]] += 1
                sum2[C[i]+D[j]] += 1

        ans = 0
        for k, v in sum1.items():
            if -k in sum2: ans += v*sum2[-k]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
