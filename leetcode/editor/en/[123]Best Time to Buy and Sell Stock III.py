#Say you have an array for which the ith element is the price of a given stock on day i. 
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions. 
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again). 
#
# Example 1: 
#
# 
#Input: [3,3,5,0,0,3,1,4]
#Output: 6
#Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3. 
#
# Example 2: 
#
# 
#Input: [1,2,3,4,5]
#Output: 4
#Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#             engaging multiple transactions at the same time. You must sell before buying again.
# 
#
# Example 3: 
#
# 
#Input: [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transaction is done, i.e. max profit = 0. 
# Related Topics Array Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<=1: return 0
        dp = [[0]*5 for _ in range(n)]
        for t in range(1,n):
            for i in range(1, 5):
                if i%2==0:
                    dp[t][i] = max(dp[t-1][i], dp[t-1][i-1]+prices[t]-prices[t-1])
                else:
                    dp[t][i] = max(dp[t-1][i]+prices[t]-prices[t-1], dp[t-1][i-1])
        return max(dp[n-1][2],dp[n-1][4])

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        gbl = [[0] * 3 for _ in range(n)]
        loc = [[0] * 3 for _ in range(n)]
        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            for j in range(1,3):
                loc[i][j] = max(gbl[i-1][j - 1] + max(0, diff), loc[i - 1][j] + diff)
                gbl[i][j] = max(gbl[i-1][j], loc[i][j])
        return gbl[n-1][2]

#leetcode submit region end(Prohibit modification and deletion)
