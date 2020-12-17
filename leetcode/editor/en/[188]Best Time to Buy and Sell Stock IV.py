#Say you have an array for which the i-th element is the price of a given stock on day i. 
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions. 
#
# Note: 
#You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again). 
#
# Example 1: 
#
# 
#Input: [2,4,1], k = 2
#Output: 2
#Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# 
#
# Example 2: 
#
# 
#Input: [3,2,6,5,0,3], k = 2
#Output: 7
#Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
#             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# 
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if 2*k>=n: return self.noLimit(prices)
        else: return self.limitK(prices, k)

    def noLimit(self, prices):
        n = len(prices)
        if n <= 1: return 0
        ans = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans

    def limitK(self, prices, k):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<=1: return 0
        dp = [[0]*(2*k+1) for _ in range(n)]
        ans = 0
        for t in range(1,n):
            for i in range(1, 2*k+1):
                if i%2==0:
                    dp[t][i] = max(dp[t-1][i], dp[t-1][i-1]+prices[t]-prices[t-1])
                    if t==n-1: ans = max(ans, dp[t][i])
                else:
                    dp[t][i] = max(dp[t-1][i]+prices[t]-prices[t-1], dp[t-1][i-1])
        return ans
#leetcode submit region end(Prohibit modification and deletion)
