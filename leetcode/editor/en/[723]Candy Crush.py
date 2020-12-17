# This question is about implementing a basic elimination algorithm for Candy Cr
# ush. 
# 
#  Given a 2D integer array board representing the grid of candy, different posi
# tive integers board[i][j] represent different types of candies. A value of board
# [i][j] = 0 represents that the cell at position (i, j) is empty. The given board
#  represents the state of the game following the player's move. Now, you need to 
# restore the board to a stable state by crushing candies according to the followi
# ng rules: 
# 
#  
#  If three or more candies of the same type are adjacent vertically or horizont
# ally, "crush" them all at the same time - these positions become empty. 
#  After crushing all candies simultaneously, if an empty space on the board has
#  candies on top of itself, then these candies will drop until they hit a candy o
# r bottom at the same time. (No new candies will drop outside the top boundary.) 
# 
#  After the above steps, there may exist more candies that can be crushed. If s
# o, you need to repeat the above steps. 
#  If there does not exist more candies that can be crushed (ie. the board is st
# able), then return the current board. 
#  
# 
#  You need to perform the above rules until the board becomes stable, then retu
# rn the current board. 
# 
#  
# 
#  Example: 
# 
#  
# Input:
# board = 
# [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,41
# 4],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[
# 4,1,4,4,1014]]
# 
# Output:
# [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,
# 113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,
# 512,713,1014]]
# 
# Explanation: 
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  The length of board will be in the range [3, 50]. 
#  The length of board[i] will be in the range [3, 50]. 
#  Each board[i][j] will initially start as an integer in the range [1, 2000]. 
#  
#  Related Topics Array Two Pointers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(board), len(board[0])

        while True:
            to_delete = []
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0: continue
                    x0=x1=i
                    y0=y1=j
                    while x0>=0 and x0> i-3 and board[x0][j]==board[i][j]: x0-=1
                    while x1<m and x1<i+3 and board[x1][j] ==board[i][j]: x1 += 1
                    while y0>=0 and y0>j-3 and board[i][y0]==board[i][j]: y0-=1
                    while y1<n and y1< j+3 and board[i][y1]==board[i][j]: y1 +=1
                    if x1-x0>3 or y1-y0>3: to_delete.append([i, j])
            if not to_delete: break
            for i, j in to_delete:
                board[i][j] = 0
            for j in range(n):
                t = m-1
                for i in range(m-1, -1, -1):
                    if board[i][j]:
                        board[i][j], board[t][j] = board[t][j], board[i][j]
                        t -=1
        return board
# leetcode submit region end(Prohibit modification and deletion)
