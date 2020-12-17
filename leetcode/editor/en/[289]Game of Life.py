#According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970." 
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article): 
#
# 
# Any live cell with fewer than two live neighbors dies, as if caused by under-population. 
# Any live cell with two or three live neighbors lives on to the next generation. 
# Any live cell with more than three live neighbors dies, as if by over-population.. 
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. 
# 
#
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. 
#
# Example: 
#
# 
#Input: 
#[
#  [0,1,0],
#  [0,0,1],
#  [1,1,1],
#  [0,0,0]
#]
#Output: 
#[
#  [0,0,0],
#  [1,0,1],
#  [0,1,1],
#  [0,1,0]
#]
# 
#
# Follow up: 
#
# 
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells. 
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems? 
# 
# Related Topics Array



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        lives = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx==0 and dy==0: continue
                        ni = i+dx
                        nj = j+dy
                        if ni<0 or ni>=m or nj<0 or nj>=n: continue
                        if board[ni][nj] == 1: lives[i][j] += 1
        for i in range(m):
            for j in range(n):
                if board[i][j]==1:
                    if lives[i][j] not in [2, 3]: board[i][j]=0
                else:
                    if lives[i][j] ==3: board[i][j] =1

        
#leetcode submit region end(Prohibit modification and deletion)
