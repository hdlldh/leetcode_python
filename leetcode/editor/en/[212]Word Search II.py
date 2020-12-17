#Given a 2D board and a list of words from the dictionary, find all words in the board. 
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. 
#
# 
#
# Example: 
#
# 
#Input: 
#board = [
#  ['o','a','a','n'],
#  ['e','t','a','e'],
#  ['i','h','k','r'],
#  ['i','f','l','v']
#]
#words = ["oath","pea","eat","rain"]
#
#Output: ["eat","oath"]
# 
#
# 
#
# Note: 
#
# 
# All inputs are consist of lowercase letters a-z. 
# The values of words are distinct. 
# 
# Related Topics Backtracking Trie



#leetcode submit region begin(Prohibit modification and deletion)
class Trie(object):
    def __init__(self):
        self.root = {}

    def insert(self, word):
        p = self.root
        for ch in word:
            p = p.setdefault(ch, {})
        p['$'] = {}

    def startsWith(self, s):
        p = self.root
        for ch in s:
            if ch not in p: return False
            p = p[ch]
        return True

    def search(self, s):
        p = self.root
        for ch in s:
            if ch not in p: return False
            p = p[ch]
        if '$' in p: return True
        return False


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        if m == 0: return []
        n = len(board[0])
        trie = Trie()
        ans = set()
        for word in words: trie.insert(word)

        def dfs(board, i, j, trie, s, ans):
            m, n = len(board), len(board[0])
            if i < 0 or i >= m or j < 0 or j >= n: return
            s += board[i][j]
            if not trie.startsWith(s): return
            if trie.search(s): ans.add(s)
            tmp = board[i][j]
            board[i][j] = '#'
            dx = [0, -1, 0, 1]
            dy = [-1, 0, 1, 0]
            for k in range(4):
                dfs(board, i + dx[k], j + dy[k], trie, s, ans)
            board[i][j] = tmp

        for i in range(m):
            for j in range(n):
                dfs(board, i, j, trie, '', ans)
        return list(ans)

#leetcode submit region end(Prohibit modification and deletion)
