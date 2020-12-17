# Given two integer arrays A and B, return the maximum length of an subarray tha
# t appears in both arrays. 
# 
#  Example 1: 
# 
#  
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= len(A), len(B) <= 1000 
#  0 <= A[i], B[i] < 100 
#  
# 
#  
#  Related Topics Array Hash Table Binary Search Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m = len(A)
        n = len(B)
        dp = [[0]*(m+1) for _ in range(n+1)]
        ans = 0
        for i in range(1,m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    ans = max(ans, dp[i][j])
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
