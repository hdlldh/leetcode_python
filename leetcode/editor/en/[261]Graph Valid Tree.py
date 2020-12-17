#Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree. 
#
# Example 1: 
#
# 
#Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
#Output: true 
#
# Example 2: 
#
# 
#Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
#Output: false 
#
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges. 
# Related Topics Depth-first Search Breadth-first Search Union Find Graph

import collections

#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validTree2(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n==1: return True
        outEdges = collections.defaultdict(set)
        visited = set()
        for u, v in edges:
            outEdges[u].add(v)
            outEdges[v].add(u)

        queue = collections.deque()
        queue.append(0)
        visited.add(0)

        while queue:
            u = queue.popleft()
            for v in outEdges[u]:
                if v in visited: return False
                queue.append(v)
                visited.add(v)
                outEdges[v].remove(u)

        if len(visited)!=n: return False
        return True

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        roots = [i for i in range(n)]
        cnt = n
        for u, v in edges:
            x = self.find(roots, u)
            y = self.find(roots, v)
            if x==y: return False
            roots[x] = y
            cnt -= 1
        return cnt == 1

    def find(self, roots, i):
        while roots[i]!= i: i = roots[i]
        return i
#leetcode submit region end(Prohibit modification and deletion)
