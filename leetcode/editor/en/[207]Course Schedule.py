#There are a total of n courses you have to take, labeled from 0 to n-1. 
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1] 
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses? 
#
# Example 1: 
#
# 
#Input: 2, [[1,0]] 
#Output: true
#Explanation: There are a total of 2 courses to take. 
#             To take course 1 you should have finished course 0. So it is possible. 
#
# Example 2: 
#
# 
#Input: 2, [[1,0],[0,1]]
#Output: false
#Explanation: There are a total of 2 courses to take. 
#             To take course 1 you should have finished course 0, and to take course 0 you should
#             also have finished course 1. So it is impossible.
# 
#
# Note: 
#
# 
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented. 
# You may assume that there are no duplicate edges in the input prerequisites. 
# 
# Related Topics Depth-first Search Breadth-first Search Graph Topological Sort



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        inDegree = collections.defaultdict(int)
        outEdges = collections.defaultdict(list)
        for t, s in prerequisites:
            inDegree[t] += 1
            outEdges[s].append(t)

        queue = collections.deque()
        visited = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
                visited.append(i)

        while queue:
            s = queue.popleft()
            for t in outEdges[s]:
                inDegree[t] -= 1
                if inDegree[t] == 0:
                    queue.append(t)
                    visited.append(t)
        return len(visited) == numCourses
#leetcode submit region end(Prohibit modification and deletion)
