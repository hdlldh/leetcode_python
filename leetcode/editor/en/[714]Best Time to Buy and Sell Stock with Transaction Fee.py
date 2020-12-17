# Your are given an array of integers prices, for which the i-th element is the 
# price of a given stock on day i; and a non-negative integer fee representing a t
# ransaction fee. 
#  You may complete as many transactions as you like, but you need to pay the tr
# ansaction fee for each transaction. You may not buy more than 1 share of a stock
#  at a time (ie. you must sell the stock share before you buy again.) 
#  Return the maximum profit you can make. 
# 
#  Example 1: 
#  
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
#  Buying at prices[0] = 1 Selling at prices[3] = 8 Buying at prices[4] = 4 Sell
# ing at prices[5] = 9 The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#  
#  
# 
#  Note:
#  0 < prices.length <= 50000. 
#  0 < prices[i] < 50000. 
#  0 <= fee < 50000. 
#  Related Topics Array Dynamic Programming Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        sold = [0] * n
        hold = [0] * n
        hold[0] = -prices[0]
        for i in range(1, n):
            sold[i] = max(sold[i-1], hold[i-1] + prices[i] - fee)
            hold[i] = max(hold[i-1], sold[i-1] - prices[i])
        return sold[-1]
        
# leetcode submit region end(Prohibit modification and deletion)
