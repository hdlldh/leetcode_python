#Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n. 
#
# Example 1: 
#
# 
#Input: n = 12
#Output: 3 
#Explanation: 12 = 4 + 4 + 4. 
#
# Example 2: 
#
# 
#Input: n = 13
#Output: 2
#Explanation: 13 = 4 + 9. Related Topics Math Dynamic Programming Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        squares = set()
        i = 1
        while i*i<=n:
            squares.add(i*i)
            i+=1

        for i in range(1, n+1):
            for j in squares:
                if j>i: continue
                dp[i] = min(dp[i], dp[i-j]+1)
        return dp[-1]
        
#leetcode submit region end(Prohibit modification and deletion)
