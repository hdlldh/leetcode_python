#
#In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
# 
#The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
# 
#The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.
# 
#Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.
# Example 1: 
# 
#Input: [[1,2], [1,3], [2,3]]
#Output: [2,3]
#Explanation: The given directed graph will be like this:
#  1
# / \
#v   v
#2-->3
# 
# 
# Example 2: 
# 
#Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
#Output: [4,1]
#Explanation: The given directed graph will be like this:
#5 <- 1 -> 2
#     ^    |
#     |    v
#     4 <- 3
# 
# 
# Note: 
# The size of the input 2D-array will be between 3 and 1000. 
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array. 
# Related Topics Tree Depth-first Search Union Find Graph



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        roots = [i for i in range(n)]
        first = []
        second = []
        parents = {}
        for p, q in edges:
            if q in parents and p != parents[q]:
                first = [parents[q], q]
                second = [p, q]
            else:
                parents[q] = p
        for p, q in edges:
            if p != parents[q]: continue
            root_p = self.find(roots, p-1)
            root_q = self.find(roots, q-1)
            if root_p==root_q:
                if not first: return [p, q]
                else: return first
            self.union(roots, p-1, q-1)
        return second


    def find(self, roots, p):
        while p!=roots[p]: p = roots[p]
        return p

    def union(self, roots, p, q):
        root_p = self.find(roots, p)
        root_q = self.find(roots, q)
        if root_p != root_q: roots[root_q] = root_p
#leetcode submit region end(Prohibit modification and deletion)
