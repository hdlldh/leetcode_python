#In the "100 game," two players take turns adding, to a running total, any integ
#er from 1..10. The player who first causes the running total to reach or exceed 
#100 wins. 
#
# What if we change the game so that players cannot re-use integers? 
#
# For example, two players might take turns drawing from a common pool of number
#s of 1..15 without replacement until they reach a total >= 100. 
#
# Given an integer maxChoosableInteger and another integer desiredTotal, determi
#ne if the first player to move can force a win, assuming both players play optim
#ally. 
#
# You can always assume that maxChoosableInteger will not be larger than 20 and 
#desiredTotal will not be larger than 300.
# 
#
# Example
# 
#Input:
#maxChoosableInteger = 10
#desiredTotal = 11
#
#Output:
#false
#
#Explanation:
#No matter which integer the first player choose, the first player will lose.
#The first player can choose an integer from 1 up to 10.
#If the first player choose 1, the second player can only choose integers from 2
# up to 10.
#The second player will win by choosing 10 and get a total = 11, which is >= des
#iredTotal.
#Same with other integers chosen by the first player, the second player will alw
#ays win.
# 
# Related Topics Dynamic Programming Minimax




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger>=desiredTotal: return True
        if maxChoosableInteger*(maxChoosableInteger+1)//2 < desiredTotal: return False
        mem = {}
        return self.helper(maxChoosableInteger, desiredTotal, 0, mem)

    def helper(self, maxChoosableInteger, desiredTotal, used, mem):
        if desiredTotal<=0: return False
        if used in mem: return mem[used]
        for i in range(1, maxChoosableInteger+1):
            cur = 1<<i
            if used & cur: continue
            if not self.helper(maxChoosableInteger, desiredTotal-i, used | cur, mem):
                mem[used] = True
                return True
        mem[used] = False
        return False

        
#leetcode submit region end(Prohibit modification and deletion)
