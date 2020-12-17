#Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph. 
#
# Example 1: 
#
# 
#Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
#     0          3
#     |          |
#     1 --- 2    4 
#
#Output: 2
# 
#
# Example 2: 
#
# 
#Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
#     0           4
#     |           |
#     1 --- 2 --- 3
#
#Output:  1
# 
#
# Note: 
#You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges. 
# Related Topics Depth-first Search Breadth-first Search Union Find Graph



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = [i for i in range(n)]
        ans = n
        for i, j in edges:
            root_i = self.find(parent, i)
            root_j = self.find(parent, j)
            if root_i!=root_j:
                self.union(parent, i, j)
                ans -= 1
        return ans


    def find(self, parent, i):
        while i!=parent[i]: i = parent[i]
        return i

    def union(self, parent, i, j):
        root_i = self.find(parent, i)
        root_j = self.find(parent, j)
        if root_i!=root_j: parent[root_j] = root_i




        
#leetcode submit region end(Prohibit modification and deletion)
