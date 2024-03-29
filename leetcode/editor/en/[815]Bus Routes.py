#We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever. 
#
# We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible. 
#
# 
#Example:
#Input: 
#routes = [[1, 2, 7], [3, 6, 7]]
#S = 1
#T = 6
#Output: 2
#Explanation: 
#The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# 
#
# Note: 
#
# 
# 1 <= routes.length <= 500. 
# 1 <= routes[i].length <= 500. 
# 0 <= routes[i][j] < 10 ^ 6. 
# 
# Related Topics Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        graph = collections.defaultdict(set)
        for route in range(len(routes)):
            for stop in routes[route]:
                graph[stop].add(route)

        if S == T: return 0
        steps = 0
        queue = collections.deque()
        queue.append(S)
        visited = set()
        visited.add(S)
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur == T: return steps
                for route in graph[cur]:
                    for nxt in routes[route]:
                        if nxt in visited: continue
                        queue.append(nxt)
                        visited.add(nxt)
            steps += 1

        return -1
#leetcode submit region end(Prohibit modification and deletion)
