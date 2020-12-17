# Given an undirected tree, return its diameter: the number of edges in a longes
# t path in that tree. 
# 
#  The tree is given as an array of edges where edges[i] = [u, v] is a bidirecti
# onal edge between nodes u and v. Each node has labels in the set {0, 1, ..., edg
# es.length}. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: edges = [[0,1],[0,2]]
# Output: 2
# Explanation: 
# A longest path of the tree is the path 1 - 0 - 2.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# Output: 4
# Explanation: 
# A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= edges.length < 10^4 
#  edges[i][0] != edges[i][1] 
#  0 <= edges[i][j] <= edges.length 
#  The given edges form an undirected tree. 
#  
#  Related Topics Tree Depth-first Search Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        leaves = [u for u in indegree if indegree[u] == 1]
        seen = set(leaves)
        queue = collections.deque(leaves)
        step = 0

        while queue:
            size = len(queue)
            if size ==1: return 2*step
            step += 1
            for _ in range(size):
                u = queue.popleft()
                for v in graph[u]:
                    indegree[v] -=1
                    if indegree[v] == 1 and v not in seen:
                        queue.append(v)
                        seen.add(v)
        return 2* step-1
        
# leetcode submit region end(Prohibit modification and deletion)
