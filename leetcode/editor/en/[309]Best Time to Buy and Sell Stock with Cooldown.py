#Say you have an array for which the ith element is the price of a given stock on day i. 
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions: 
#
# 
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again). 
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day) 
# 
#
# Example: 
#
# 
#Input: [1,2,3,0,2]
#Output: 3 
#Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## hold[i] = max(hold[i-1], rest[i-1]-prices[i-1])
        ## sold[i] = hold[i-1] + prices[i-1]
        ## rest[i] = max(rest[i-1], sold[i-1])
        n = len(prices)
        hold = [0] * (n+1)
        sold = [0] * (n+1)
        rest = [0] * (n+1)
        hold[0] = -float('inf')
        for i in range(1, n+1):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i - 1])
            #sold[i] = hold[i - 1] + prices[i - 1]
            sold[i] = max(sold[i-1], hold[i - 1] + prices[i - 1])
            #rest[i] = max(rest[i - 1], sold[i - 1])
            rest[i] = max(rest[i - 1], sold[i - 1])
        return max(sold[n], rest[n])

        
#leetcode submit region end(Prohibit modification and deletion)
