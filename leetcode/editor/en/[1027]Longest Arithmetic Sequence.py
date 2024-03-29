# Given an array A of integers, return the length of the longest arithmetic subs
# equence in A. 
# 
#  Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <
# = i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if 
# B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1). 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [3,6,9,12]
# Output: 4
# Explanation: 
# The whole array is an arithmetic sequence with steps of length = 3.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [9,4,7,2,10]
# Output: 3
# Explanation: 
# The longest arithmetic subsequence is [4,7,10].
#  
# 
#  
#  Example 3: 
# 
#  
# Input: [20,1,15,3,10,5,8]
# Output: 4
# Explanation: 
# The longest arithmetic subsequence is [20,15,10,5].
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  2 <= A.length <= 2000 
#  0 <= A[i] <= 10000 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n<=1: return n
        count = {}
        ans = 1
        for i in range(1, n):
            for j in range(i):
                gap = A[i] - A[j]
                if (gap, j) not in count:
                    count[(gap, i)] = 2
                else:
                    count[(gap, i)] = count[(gap, j)] + 1
                ans = max(ans, count[(gap, i)])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
