# A game on an undirected graph is played by two players, Mouse and Cat, who alt
# ernate turns. 
# 
#  The graph is given as follows: graph[a] is a list of all nodes b such that ab
#  is an edge of the graph. 
# 
#  Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, 
# and there is a Hole at node 0. 
# 
#  During each player's turn, they must travel along one edge of the graph that 
# meets where they are. For example, if the Mouse is at node 1, it must travel to 
# any node in graph[1]. 
# 
#  Additionally, it is not allowed for the Cat to travel to the Hole (node 0.) 
# 
#  Then, the game can end in 3 ways: 
# 
#  
#  If ever the Cat occupies the same node as the Mouse, the Cat wins. 
#  If ever the Mouse reaches the Hole, the Mouse wins. 
#  If ever a position is repeated (ie. the players are in the same position as a
#  previous turn, and it is the same player's turn to move), the game is a draw. 
#  
# 
#  Given a graph, and assuming both players play optimally, return 1 if the game
#  is won by Mouse, 2 if the game is won by Cat, and 0 if the game is a draw. 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# Output: 0
# Explanation:
# 4---3---1
# |   |
# 2---5
#  \ /
#   0
#  
# 
#  
# 
#  Note: 
# 
#  
#  3 <= graph.length <= 50 
#  It is guaranteed that graph[1] is non-empty. 
#  It is guaranteed that graph[2] contains a non-zero element. 
#  
#  
#  Related Topics Breadth-first Search Minimax


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        mem = {}
        return self.dfs(graph, 0, 1, 2, mem)

    def dfs(self, graph, t, m, c, mem):
        if t == len(graph) * 2: return 0
        if m == 0: return 1
        if m == c: return 2
        if (t, m, c) in mem: return mem[(t, m, c)]
        mouseTurn = t % 2 == 0
        if mouseTurn:
            catWin = True
            for nxt in graph[m]:
                ans = self.dfs(graph, t + 1, nxt, c, mem)
                if ans == 1:
                    mem[(t, m, c)] = 1
                    return mem[(t, m, c)]
                elif ans != 2:
                    catWin = False
            if catWin:
                mem[(t, m, c)] = 2
            else:
                mem[(t, m, c)] = 0
            return mem[(t, m, c)]
        else:
            mouseWin = True
            for nxt in graph[c]:
                if nxt == 0: continue
                ans = self.dfs(graph, t + 1, m, nxt, mem)
                if ans == 2:
                    mem[(t, m, c)] = 2
                    return mem[(t, m, c)]
                elif ans != 1:
                    mouseWin = False
            if mouseWin:
                mem[(t, m, c)] = 1
            else:
                mem[(t, m, c)] = 0
            return mem[(t, m, c)]
        
# leetcode submit region end(Prohibit modification and deletion)
