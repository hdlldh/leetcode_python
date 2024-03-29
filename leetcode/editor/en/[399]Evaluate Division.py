#Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0. 
#
# Example: 
#Given a / b = 2.0, b / c = 3.0. 
#queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
#return [6.0, 0.5, -1.0, 1.0, -1.0 ]. 
#
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>. 
#
# According to the example above: 
#
# 
#equations = [ ["a", "b"], ["b", "c"] ],
#values = [2.0, 3.0],
#queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
#
# 
#
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction. 
# Related Topics Union Find Graph



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        n = len(equations)
        graph = collections.defaultdict(set)
        weight = {}
        for i in range(n):
            p = equations[i][0]
            q = equations[i][1]
            graph[p].add(q)
            weight[(p, q)] = values[i]
            graph[q].add(p)
            weight[(q, p)] = 1.0/values[i]

        ans = []
        for p, q in queries:
            if p not in graph or q not in graph: ans.append(-1.0)
            elif p== q: ans.append(1.0)
            else: ans.append(self.bfs(graph, weight, p, q))
        return ans

    def bfs(self, graph, weight, p, q):
        queue = collections.deque()
        queue.append([p, 1.0])
        visited = set()
        visited.add(p)
        while queue:
            p, val = queue.popleft()
            for k in graph[p]:
                if k in visited: continue
                if k == q: return val* weight[(p, k)]
                queue.append([k, val*weight[(p, k)]])
                visited.add(k)
        return -1


#leetcode submit region end(Prohibit modification and deletion)
