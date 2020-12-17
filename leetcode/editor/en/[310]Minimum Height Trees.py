#For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels. 
#
# Format 
#The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels). 
#
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges. 
#
# Example 1 : 
#
# 
#Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#
#        0
#        |
#        1
#       / \
#      2   3 
#
#Output: [1]
# 
#
# Example 2 : 
#
# 
#Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#
#     0  1  2
#      \ | /
#        3
#        |
#        4
#        |
#        5 
#
#Output: [3, 4] 
#
# Note: 
#
# 
# According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.” 
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf. 
# 
# Related Topics Breadth-first Search Graph



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n==1: return [0]
        inDegree = collections.defaultdict(int)
        outEdges = collections.defaultdict(set)
        for u, v in edges:
            inDegree[u] += 1
            inDegree[v] += 1
            outEdges[u].add(v)
            outEdges[v].add(u)

        queue = collections.deque()
        for i in range(n):
            if inDegree[i] == 1: queue.append(i)
        ans = []
        while queue:
            ans = list(queue)
            for _ in range(len(queue)):
                u = queue.popleft()
                for v in outEdges[u]:
                    inDegree[v] -= 1
                    if inDegree[v] == 1: queue.append(v)
        return ans

#leetcode submit region end(Prohibit modification and deletion)
