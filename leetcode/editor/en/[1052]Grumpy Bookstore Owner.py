#Today, the bookstore owner has a store open for customers.length minutes. Every
# minute, some number of customers (customers[i]) enter the store, and all those 
#customers leave after the end of that minute. 
#
# On some minutes, the bookstore owner is grumpy. If the bookstore owner is grum
#py on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0. When the bookstor
#e owner is grumpy, the customers of that minute are not satisfied, otherwise the
#y are satisfied. 
#
# The bookstore owner knows a secret technique to keep themselves not grumpy for
# X minutes straight, but can only use it once. 
#
# Return the maximum number of customers that can be satisfied throughout the da
#y. 
#
# 
#
# Example 1: 
#
# 
#Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
#Output: 16
#Explanation: The bookstore owner keeps themselves not grumpy for the last 3 min
#utes. 
#The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 =
# 16.
# 
#
# 
#
# Note: 
#
# 
# 1 <= X <= customers.length == grumpy.length <= 20000 
# 0 <= customers[i] <= 1000 
# 0 <= grumpy[i] <= 1 
# Related Topics Array Sliding Window




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        n = len(customers)
        ans = 0
        for i in range(n):
            if grumpy[i]==0: ans += customers[i]
        mx = 0

        for i in range(X):
            if grumpy[i]==1: mx += customers[i]
        t = mx
        for i in range(X, n):
            if grumpy[i-X]==1: t-=customers[i-X]
            if grumpy[i] ==1: t+=customers[i]
            mx = max(mx, t)
        return ans + mx

        
#leetcode submit region end(Prohibit modification and deletion)
