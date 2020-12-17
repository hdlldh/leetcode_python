#Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. 
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region. 
#
# Example: 
#
# 
#X X X X
#X O O X
#X X O X
#X O X X
# 
#
# After running your function, the board should be: 
#
# 
#X X X X
#X X X X
#X X X X
#X O X X
# 
#
# Explanation: 
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically. 
# Related Topics Depth-first Search Breadth-first Search Union Find



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m==0: return
        n = len(board[0])
        for i in range(m):
            self.dfs(board, i, 0)
            self.dfs(board, i, n-1)
        for j in range(n):
            self.dfs(board, 0, j)
            self.dfs(board, m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j]=='D': board[i][j]= 'O'
                elif board[i][j]=='O': board[i][j]='X'

    def dfs(self, board, i, j):
        m, n = len(board), len(board[0])
        if i<0 or i>=m or j<0 or j>=n: return
        if board[i][j]!= 'O': return
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        board[i][j] = 'D'
        for k in range(4):
            self.dfs(board, i+dx[k], j+dy[k])
#leetcode submit region end(Prohibit modification and deletion)
