# Alice plays the following game, loosely based on the card game "21". 
# 
#  Alice starts with 0 points, and draws numbers while she has less than K point
# s. During each draw, she gains an integer number of points randomly from the ran
# ge [1, W], where W is an integer. Each draw is independent and the outcomes have
#  equal probabilities. 
# 
#  Alice stops drawing numbers when she gets K or more points. What is the proba
# bility that she has N or less points? 
# 
#  Example 1: 
# 
#  
# Input: N = 10, K = 1, W = 10
# Output: 1.00000
# Explanation:  Alice gets a single card, then stops.
#  
# 
#  Example 2: 
# 
#  
# Input: N = 6, K = 1, W = 10
# Output: 0.60000
# Explanation:  Alice gets a single card, then stops.
# In 6 out of W = 10 possibilities, she is at or below N = 6 points.
#  
# 
#  Example 3: 
# 
#  
# Input: N = 21, K = 17, W = 10
# Output: 0.73278 
# 
#  Note: 
# 
#  
#  0 <= K <= N <= 10000 
#  1 <= W <= 10000 
#  Answers will be accepted as correct if they are within 10^-5 of the correct a
# nswer. 
#  The judging time limit has been reduced for this question. 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K==0: return 1.0
        dp = [0] * (N+1)
        dp[0] = 1.0
        sm = [0] * (N+1)
        sm[0] = 1.0
        for i in range(1, N+1):
            left = max(0, i-W)
            right = min(K-1, i-1)
            if left <= right:
                if left==0: dp[i]=sm[right]/W
                else: dp[i] = (sm[right]-sm[left-1])/W
            sm[i] = sm[i-1] + dp[i]
        return sm[N] - sm[K-1]
# leetcode submit region end(Prohibit modification and deletion)
