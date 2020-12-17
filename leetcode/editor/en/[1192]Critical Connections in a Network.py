#There are n servers numbered from 0 to n-1 connected by undirected server-to-se
#rver connections forming a network where connections[i] = [a, b] represents a co
#nnection between servers a and b. Any server can reach any other server directly
# or indirectly through the network. 
#
# A critical connection is a connection that, if removed, will make some server 
#unable to reach some other server. 
#
# Return all critical connections in the network in any order. 
#
# 
# Example 1: 
#
# 
#
# 
#Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
#Output: [[1,3]]
#Explanation: [[3,1]] is also accepted.
# 
#
# 
# Constraints: 
#
# 
# 1 <= n <= 10^5 
# n-1 <= connections.length <= 10^5 
# connections[i][0] != connections[i][1] 
# There are no repeated connections. 
# 
# Related Topics Depth-first Search




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = collections.defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        self.id = 0
        ids = [-1]*n
        low = [float('inf')]*n
        ans = []

        def dfs(graph, u, ids, low, parent, ans):
            ids[u] = self.id
            low[u] = self.id
            self.id+=1
            for v in graph[u]:
                if v==parent: continue
                if ids[v] == -1:
                    dfs(graph, v, ids, low, u, ans)
                    low[u] = min(low[u], low[v])
                    if low[v] > ids[u]:
                        ans.append([u, v])
                else:
                    low[u] = min(low[u], ids[v])

        for i in range(n):
            if ids[i] == -1:
                dfs(graph, i, ids, low, -1, ans)
        return ans
#leetcode submit region end(Prohibit modification and deletion)
