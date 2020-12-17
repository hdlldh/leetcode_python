# A Tic-Tac-Toe board is given as a string array board. Return True if and only 
# if it is possible to reach this board position during the course of a valid tic-
# tac-toe game. 
# 
#  The board is a 3 x 3 array, and consists of characters " ", "X", and "O". The
#  " " character represents an empty square. 
# 
#  Here are the rules of Tic-Tac-Toe: 
# 
#  
#  Players take turns placing characters into empty squares (" "). 
#  The first player always places "X" characters, while the second player always
#  places "O" characters. 
#  "X" and "O" characters are always placed into empty squares, never filled one
# s. 
#  The game ends when there are 3 of the same (non-empty) character filling any 
# row, column, or diagonal. 
#  The game also ends if all squares are non-empty. 
#  No more moves can be played if the game is over. 
#  
# 
#  
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".
# 
# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.
# 
# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false
# 
# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
#  
# 
#  Note: 
# 
#  
#  board is a length-3 array of strings, where each string board[i] has length 3
# . 
#  Each board[i][j] is a character in the set {" ", "X", "O"}. 
#  
#  Related Topics Math Recursion


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """

        nx = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    nx += 1
                elif board[i][j] == 'O':
                    nx -= 1
        if nx not in [0, 1]: return False
        if self.win(board, 'X') and nx != 1: return False
        if self.win(board, 'O') and nx != 0: return False
        return True

    def win(self, board, ch):
        rows = [0] * 3
        cols = [0] * 3
        diag1 = 0
        diag2 = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == ch:
                    rows[i] += 1
                    cols[j] += 1
                    if i == j: diag1 += 1
                    if i + j == 2: diag2 += 1
                    if 3 in [rows[i], cols[j], diag1, diag2]: return True
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
