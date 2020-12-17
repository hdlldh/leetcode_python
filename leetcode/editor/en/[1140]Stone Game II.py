# Alex and Lee continue their games with piles of stones. There are a number of 
# piles arranged in a row, and each pile has a positive integer number of stones p
# iles[i]. The objective of the game is to end with the most stones. 
# 
#  Alex and Lee take turns, with Alex starting first. Initially, M = 1. 
# 
#  On each player's turn, that player can take all the stones in the first X rem
# aining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). 
# 
#  The game continues until all the stones have been taken. 
# 
#  Assuming Alex and Lee play optimally, return the maximum number of stones Ale
# x can get. 
# 
#  
#  Example 1: 
# 
#  
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, th
# en Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex
#  takes two piles at the beginning, then Lee can take all three piles left. In th
# is case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= piles.length <= 100 
#  1 <= piles[i] <= 10 ^ 4 
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        mem = {}
        self.helper(piles, 0, 1, mem)
        return (sum(piles) + mem[(0, 1)]) // 2

    def helper(self, piles, start, M, mem):
        N = len(piles)
        if start >= N: return 0
        if N - start <= 2 * M:
            return sum(piles[start:])
        if (start, M) in mem: return mem[(start, M)]
        cur_sum = 0
        mem[(start, M)] = -float('inf')
        for x in range(1, M * 2 + 1):
            cur_sum += piles[start + x - 1]
            mem[(start, M)] = max(mem[(start, M)], cur_sum - self.helper(piles, start + x, max(M, x), mem))

        return mem[(start, M)]
        
# leetcode submit region end(Prohibit modification and deletion)
