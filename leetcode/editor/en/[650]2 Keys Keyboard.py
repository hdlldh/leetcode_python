# Initially on a notepad only one character 'A' is present. You can perform two 
# operations on this notepad for each step: 
# 
#  
#  Copy All: You can copy all the characters present on the notepad (partial cop
# y is not allowed). 
#  Paste: You can paste the characters which are copied last time. 
#  
# 
#  
# 
#  Given a number n. You have to get exactly n 'A' on the notepad by performing 
# the minimum number of steps permitted. Output the minimum number of steps to get
#  n 'A'. 
# 
#  Example 1: 
# 
#  
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The n will be in the range [1, 1000]. 
#  
# 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)

        for i in range(2,n+1):
            dp[i] = i
            for j in range(2, i):
                if i%j==0:
                    dp[i] = min(dp[i], dp[j] + i//j)
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
