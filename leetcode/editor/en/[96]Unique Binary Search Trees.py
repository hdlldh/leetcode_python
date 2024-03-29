#Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n? 
#
# Example: 
#
# 
#Input: 3
#Output: 5
#Explanation:
#Given n = 3, there are a total of 5 unique BST's:
#
#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3
# 
# Related Topics Dynamic Programming Tree



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1: return 1
        dp = [0]*(n+1)
        dp[0] =1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
        
#leetcode submit region end(Prohibit modification and deletion)
