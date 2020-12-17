#Write a program to solve a Sudoku puzzle by filling the empty cells. 
#
# A sudoku solution must satisfy all of the following rules: 
#
# 
# Each of the digits 1-9 must occur exactly once in each row. 
# Each of the digits 1-9 must occur exactly once in each column. 
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid. 
# 
#
# Empty cells are indicated by the character '.'. 
#
# 
#A sudoku puzzle... 
#
# 
#...and its solution numbers marked in red. 
#
# Note: 
#
# 
# The given board contain only digits 1-9 and the character '.'. 
# You may assume that the given Sudoku puzzle will have a single unique solution. 
# The given board size is always 9x9. 
# 
# Related Topics Hash Table Backtracking


import collections
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grids = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    grids[i//3*3+j//3].add(board[i][j])
        self.dfs(board, 0, 0, rows, cols, grids)

    def isValid(self, i, j, num, rows, cols, grids):
        if num in rows[i]: return False
        if num in cols[j]: return False
        if num in grids[i//3*3+j//3]: return False
        return True

    def dfs(self, board, i, j,rows, cols, grids):
        if i==9: return True
        if j==9: return self.dfs(board,i+1,0,rows,cols,grids)
        if board[i][j]=='.':
            for num in range(1,10):
                t = str(num)
                if self.isValid(i, j, t, rows, cols, grids):
                    board[i][j] = t
                    rows[i].add(t)
                    cols[j].add(t)
                    grids[i//3*3+j//3].add(t)
                    if self.dfs(board,i,j+1,rows,cols,grids): return True
                    board[i][j] = '.'
                    rows[i].remove(t)
                    cols[j].remove(t)
                    grids[i//3*3+j//3].remove(t)
            return False
        else:
            return self.dfs(board, i, j+1, rows, cols, grids)

        
#leetcode submit region end(Prohibit modification and deletion)
