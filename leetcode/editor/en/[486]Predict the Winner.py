#Given an array of scores that are non-negative integers. Player 1 picks one of 
#the numbers from either end of the array followed by the player 2 and then playe
#r 1 and so on. Each time a player picks a number, that number will not be availa
#ble for the next player. This continues until all the scores have been chosen. T
#he player with the maximum score wins. 
#
# Given an array of scores, predict whether player 1 is the winner. You can assu
#me each player plays to maximize his score. 
#
# Example 1: 
# 
#Input: [1, 5, 2]
#Output: False
#Explanation: Initially, player 1 can choose between 1 and 2. If he chooses 2 (o
#r 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then 
#player 1 will be left with 1 (or 2). So, final score of player 1 is 1 + 2 = 3, a
#nd player 2 is 5. Hence, player 1 will never be the winner and you need to retur
#n False.
# 
# 
#
# Example 2: 
# 
#Input: [1, 5, 233, 7]
#Output: True
#Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 a
#nd 7. No matter which number player 2 choose, player 1 can choose 233. Finally, 
#player 1 has more score (234) than player 2 (12), so you need to return True rep
#resenting player1 can win.
# 
# 
#
# Note: 
# 
# 1 <= length of the array <= 20. 
# Any scores in the given array are non-negative integers and will not exceed 10
#,000,000. 
# If the scores of both players are equal, then player 1 is still the winner. 
# 
# Related Topics Dynamic Programming Minimax




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.helper(nums, 0, len(nums)-1, {})>=0

    def helper(self, nums, l, r, mem):
        if l==r: return nums[l]
        n = len(nums)
        if (l, r) in mem: return mem[(l,r)]
        mem[(l, r)] = max(nums[l]-self.helper(nums, l+1, r, mem), nums[r]-self.helper(nums, l, r-1, mem))
        return mem[(l, r)]
        
#leetcode submit region end(Prohibit modification and deletion)
