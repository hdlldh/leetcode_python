#Given an undirected graph, return true if and only if it is bipartite. 
#
# Recall that a graph is bipartite if we can split it's set of nodes into two in
#dependent subsets A and B such that every edge in the graph has one node in A an
#d another node in B. 
#
# The graph is given in the following form: graph[i] is a list of indexes j for 
#which the edge between nodes i and j exists. Each node is an integer between 0 a
#nd graph.length - 1. There are no self edges or parallel edges: graph[i] does no
#t contain i, and it doesn't contain any element twice. 
#
# 
#Example 1:
#Input: [[1,3], [0,2], [1,3], [0,2]]
#Output: true
#Explanation: 
#The graph looks like this:
#0----1
#|    |
#|    |
#3----2
#We can divide the vertices into two groups: {0, 2} and {1, 3}.
# 
#
# 
#Example 2:
#Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
#Output: false
#Explanation: 
#The graph looks like this:
#0----1
#| \  |
#|  \ |
#3----2
#We cannot find a way to divide the set of nodes into two independent subsets.
# 
#
# 
#
# Note: 
#
# 
# graph will have length in range [1, 100]. 
# graph[i] will contain integers in range [0, graph.length - 1]. 
# graph[i] will not contain i or duplicate values. 
# The graph is undirected: if any element j is in graph[i], then i will be in gr
#aph[j]. 
# 
# Related Topics Depth-first Search Breadth-first Search Graph




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isBipartite2(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colors = [0] *n
        for i in range(n):
            if colors[i]==0 and not self.dfs(graph, colors, i, 1): return False
        return True

    def dfs(self, graph, colors, i, color):
        if colors[i] == 0:
            colors[i] = color
            for j in graph[i]:
                if not self.dfs(graph, colors, j, -color): return False
            return True
        else: return colors[i]==color

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colors = [0] *n
        for i in range(n):
            if colors[i]==0:
                queue = collections.deque()
                queue.append(i)
                colors[i] =1
                while queue:
                    i = queue.popleft()
                    for j in graph[i]:
                        if colors[j] == colors[i]: return False
                        if colors[j] != 0: continue
                        queue.append(j)
                        colors[j] = -colors[i]
        return True
        
#leetcode submit region end(Prohibit modification and deletion)
