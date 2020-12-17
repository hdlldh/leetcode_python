# We have a collection of rocks, each rock has a positive integer weight. 
# 
#  Each turn, we choose any two rocks and smash them together. Suppose the stone
# s have weights x and y with x <= y. The result of this smash is: 
# 
#  
#  If x == y, both stones are totally destroyed; 
#  If x != y, the stone of weight x is totally destroyed, and the stone of weigh
# t y has new weight y-x. 
#  
# 
#  At the end, there is at most 1 stone left. Return the smallest possible weigh
# t of this stone (the weight is 0 if there are no stones left.) 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0 so the array converts to [1] then that's the o
# ptimal value.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= stones.length <= 30 
#  1 <= stones[i] <= 100 
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        s = sum(stones)
        dp = [False] * (s // 2 + 1)
        dp[0] = True
        for i, stone in enumerate(stones):
            for j in range(s // 2, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]

        for i in xrange(s // 2, -1, -1):
            if dp[i]: return s - i - i
        
# leetcode submit region end(Prohibit modification and deletion)
