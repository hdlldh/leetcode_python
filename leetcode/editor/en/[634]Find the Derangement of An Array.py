# 
# In combinatorial mathematics, a derangement is a permutation of the elements o
# f a set, such that no element appears in its original position.
#  
# 
#  
# There's originally an array consisting of n integers from 1 to n in ascending 
# order, you need to find the number of derangement it can generate.
#  
# 
#  
# Also, since the answer may be very large, you should return the output mod 109
#  + 7.
#  
# 
#  Example 1: 
#  
# Input: 3
# Output: 2
# Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] a
# nd [3,1,2].
#  
#  
# 
#  Note: 
# n is in the range of [1, 106].
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        if n ==2: return 1
        dp = [0] *(n+1)
        dp[1] = 0
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = ((dp[i-1]+dp[i-2]) * (i-1)) % 1000000007
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
