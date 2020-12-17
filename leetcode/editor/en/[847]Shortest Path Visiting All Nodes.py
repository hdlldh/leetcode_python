#An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph. 
#
# graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected. 
#
# Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges. 
#
# 
#
# 
# 
#
# Example 1: 
#
# 
#Input: [[1,2,3],[0],[0],[0]]
#Output: 4
#Explanation: One possible path is [1,0,2,0,3] 
#
# Example 2: 
#
# 
#Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
#Output: 4
#Explanation: One possible path is [0,1,4,2,3]
# 
#
# 
#
# Note: 
#
# 
# 1 <= graph.length <= 12 
# 0 <= graph[i].length < graph.length 
# 
# Related Topics Dynamic Programming Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        queue = collections.deque()
        for i in range(n):
            queue.append([i, 1 << i])
        steps = 0
        target = (1 << n) - 1
        visited = [[0] * (1 << n) for _ in range(n)]
        while queue:
            size = len(queue)
            for _ in range(size):
                u, status = queue.popleft()
                if status == target: return steps
                for v in graph[u]:
                    t = status | 1 << v
                    if visited[v][t] == 1: continue
                    visited[v][t] = 1
                    queue.append([v, t])
            steps += 1
        return -1
#leetcode submit region end(Prohibit modification and deletion)
