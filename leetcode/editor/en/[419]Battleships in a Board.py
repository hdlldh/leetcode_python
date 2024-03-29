# Given an 2D board, count how many battleships are in it. The battleships are r
# epresented with 'X's, empty slots are represented with '.'s. You may assume the 
# following rules:
# 
#  
#  You receive a valid board, made of only battleships or empty slots. 
#  Battleships can only be placed horizontally or vertically. In other words, th
# ey can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column
# ), where N can be of any size. 
#  At least one horizontal or vertical cell separates between two battleships - 
# there are no adjacent battleships. 
#  
# 
#  Example: 
#  X..X
# ...X
# ...X
#  
# In the above board there are 2 battleships.
# 
#  Invalid Example: 
#  ...X
# XXXX
# ...X
#  
# This is an invalid board that you will not receive - as battleships will alway
# s have a cell separating between them.
#  
#  Follow up: Could you do it in one-pass, using only O(1) extra memory and with
# out modifying the value of the board?


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] =='.' or i>0 and board[i-1][j]=='X' or j>0 and board[i][j-1]=='X':continue
                ans += 1
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
