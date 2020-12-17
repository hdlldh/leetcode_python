#Given a set of N people (numbered 1, 2, ..., N), we would like to split everyon
#e into two groups of any size. 
#
# Each person may dislike some other people, and they should not go into the sam
#e group. 
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the peopl
#e numbered a and b into the same group. 
#
# Return true if and only if it is possible to split everyone into two groups in
# this way. 
#
# 
#
# 
# 
# 
# 
# 
# 
#
# 
# Example 1: 
#
# 
#Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
#Output: true
#Explanation: group1 [1,4], group2 [2,3]
# 
#
# 
# Example 2: 
#
# 
#Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
#Output: false
# 
#
# 
# Example 3: 
#
# 
#Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
#Output: false
# 
#
# 
#
# Note: 
#
# 
# 1 <= N <= 2000 
# 0 <= dislikes.length <= 10000 
# 1 <= dislikes[i][j] <= N 
# dislikes[i][0] < dislikes[i][1] 
# There does not exist i != j for which dislikes[i] == dislikes[j]. 
# 
# 
# 
# 
# Related Topics Depth-first Search




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def possibleBipartition2(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        for u, v in dislikes:
            graph[u-1].add(v-1)
            graph[v-1].add(u-1)

        colors = [0] * N
        for i in range(N):
            if colors[i]==0 and not self.dfs(graph, i, 1, colors): return False
        return True

    def dfs(self, graph, i, color, colors):
        if colors[i] == 0:
            colors[i] = color
            for j in graph[i]:
                if not self.dfs(graph, j, -color, colors): return False
            return True
        else:
            return color == colors[i]

    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        for u, v in dislikes:
            graph[u - 1].add(v - 1)
            graph[v - 1].add(u - 1)

        colors = [0] * N
        for i in range(N):
            if colors[i]==0:
                queue = collections.deque()
                queue.append(i)
                colors[i] = 1
                while queue:
                    i = queue.popleft()
                    for j in graph[i]:
                        if colors[j] == colors[i]: return False
                        if colors[j]!=0: continue
                        queue.append(j)
                        colors[j] = -colors[i]
        return True

#leetcode submit region end(Prohibit modification and deletion)
