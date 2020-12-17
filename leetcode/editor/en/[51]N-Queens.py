#The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other. 
#
# 
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. 
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively. 
#
# Example: 
#
# 
#Input: 4
#Output: [
# [".Q..",  // Solution 1
#  "...Q",
#  "Q...",
#  "..Q."],
#
# ["..Q.",  // Solution 2
#  "Q...",
#  "...Q",
#  ".Q.."]
#]
#Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
# 
# Related Topics Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.']*n for _ in range(n)]
        cols = [False] * n
        diag1 = [False] * (2*n-1)
        diag2 = [False] * (2*n-1)
        ans = []

        def dfs(board, y, ans):
            if y==n:
                tmp = []
                for i in range(n): tmp.append(''.join(board[i]))
                ans.append(tmp)
                return
            for x in range(n):
                if cols[x] == True or diag1[x+y] == True or diag2[x-y+n-1] == True: continue
                board[y][x] = 'Q'
                cols[x] = True
                diag1[x + y] = True
                diag2[x - y + n-1] = True
                dfs(board, y+1, ans)
                board[y][x] = '.'
                cols[x] = False
                diag1[x + y] = False
                diag2[x - y + n - 1] = False

        dfs(board, 0, ans)
        return ans

#leetcode submit region end(Prohibit modification and deletion)
