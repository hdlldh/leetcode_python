#Given a 2D board and a word, find if the word exists in the grid. 
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. 
#
# Example: 
#
# 
#board =
#[
#  ['A','B','C','E'],
#  ['S','F','C','S'],
#  ['A','D','E','E']
#]
#
#Given word = "ABCCED", return true.
#Given word = "SEE", return true.
#Given word = "ABCB", return false.
# 
# Related Topics Array Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0: return False
        n = len(board[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        def dfs(board, i, j, word, k):
            m, n = len(board), len(board[0])
            if i < 0 or i >= m or j < 0 or j >= n: return False
            if board[i][j] == word[k]:
                if k == len(word) - 1: return True
                tmp = board[i][j]
                board[i][j] = '#'
                for d in range(4):
                    x = i + dx[d]
                    y = j + dy[d]
                    if dfs(board, x, y, word, k + 1): return True
                board[i][j] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if dfs(board, i, j, word, 0):
                    return True
        return False

        
#leetcode submit region end(Prohibit modification and deletion)
