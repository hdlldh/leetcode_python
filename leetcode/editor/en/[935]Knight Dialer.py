# A chess knight can move as indicated in the chess diagram below: 
# 
#  . 
# 
#  
# 
#  This time, we place our chess knight on any numbered key of a phone pad (indi
# cated above), and the knight makes N-1 hops. Each hop must be from one key to an
# other numbered key. 
# 
#  Each time it lands on a key (including the initial placement of the knight), 
# it presses the number of that key, pressing N digits total. 
# 
#  How many distinct numbers can you dial in this manner? 
# 
#  Since the answer may be large, output the answer modulo 10^9 + 7. 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: 1
# Output: 10
#  
# 
#  
#  Example 2: 
# 
#  
# Input: 2
# Output: 20
#  
# 
#  
#  Example 3: 
# 
#  
# Input: 3
# Output: 46
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= N <= 5000 
#  
#  
#  
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        kmod = 1000000007
        dp = [[1 for _ in range(3)] for _ in range(4)]
        dp[3][0] = 0
        dp[3][2] = 0
        dirs = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]
        for _ in range(N-1):
            tmp = [[0 for _ in range(3)] for _ in range(4)]
            for i in range(4):
                for j in range(3):
                    for k in range(8):
                        ti = i + dirs[k][0]
                        tj = j + dirs[k][1]
                        if ti<0 or ti>=4 or tj<0 or tj>=3: continue
                        tmp[ti][tj] = (tmp[ti][tj] + dp[i][j]) % kmod
            dp = tmp
            dp[3][0] = 0
            dp[3][2] = 0
        ans = 0
        for i  in range(4):
            for j in range(3):
                ans =  (ans + dp[i][j]) % kmod
        return ans


        
# leetcode submit region end(Prohibit modification and deletion)
