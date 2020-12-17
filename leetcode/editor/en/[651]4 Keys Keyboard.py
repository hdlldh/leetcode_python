# Imagine you have a special keyboard with the following keys: 
#  Key 1: (A): Print one 'A' on screen. 
#  Key 2: (Ctrl-A): Select the whole screen. 
#  Key 3: (Ctrl-C): Copy selection to buffer. 
#  Key 4: (Ctrl-V): Print buffer on screen appending it after what has already b
# een printed. 
# 
# 
# 
#  Now, you can only press the keyboard for N times (with the above four keys), 
# find out the maximum numbers of 'A' you can print on screen. 
# 
# 
#  Example 1: 
#  
# Input: N = 3
# Output: 3
# Explanation: 
# We can at most get 3 A's on screen by pressing following key sequence:
# A, A, A
#  
#  
# 
#  Example 2: 
#  
# Input: N = 7
# Output: 9
# Explanation: 
# We can at most get 9 A's on screen by pressing following key sequence:
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
#  
#  
# 
#  Note: 
#  
#  1 <= N <= 50 
#  Answers will be in the range of 32-bit signed integer. 
#  
#  
#  Related Topics Math Dynamic Programming Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0] * (N+1)
        for i in range(1, N+1):
            dp[i] = i
            for j in range(1,i-1):
                dp[i] = max(dp[i], dp[j]*(i-j-1))
        return dp[-1]
        
# leetcode submit region end(Prohibit modification and deletion)
