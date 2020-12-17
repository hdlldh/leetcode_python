# A die simulator generates a random number from 1 to 6 for each roll. You intro
# duced a constraint to the generator such that it cannot roll the number i more t
# han rollMax[i] (1-indexed) consecutive times. 
# 
#  Given an array of integers rollMax and an integer n, return the number of dis
# tinct sequences that can be obtained with exact n rolls. 
# 
#  Two sequences are considered different if at least one element differs from e
# ach other. Since the answer may be too large, return it modulo 10^9 + 7. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2, rollMax = [1,1,2,2,2,3]
# Output: 34
# Explanation: There will be 2 rolls of die, if there are no constraints on the 
# die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMa
# x array, the numbers 1 and 2 appear at most once consecutively, therefore sequen
# ces (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2, rollMax = [1,1,1,1,1,1]
# Output: 30
#  
# 
#  Example 3: 
# 
#  
# Input: n = 3, rollMax = [1,1,1,2,2,3]
# Output: 181
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 5000 
#  rollMax.length == 6 
#  1 <= rollMax[i] <= 15 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        
# leetcode submit region end(Prohibit modification and deletion)
