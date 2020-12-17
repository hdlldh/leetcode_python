#You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where: 
#
# 
# Each 0 marks an empty land which you can pass by freely. 
# Each 1 marks a building which you cannot pass through. 
# Each 2 marks an obstacle which you cannot pass through. 
# 
#
# Example: 
#
# 
#Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#
#1 - 0 - 2 - 0 - 1
#|   |   |   |   |
#0 - 0 - 0 - 0 - 0
#|   |   |   |   |
#0 - 0 - 1 - 0 - 0
#
#Output: 7 
#
#Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
#             the point (1,2) is an ideal empty land to build a house, as the total 
#             travel distance of 3+3+1=7 is minimal. So return 7. 
#
# Note: 
#There will be at least one building. If it is not possible to build such house according to the above rules, return -1. 
# Related Topics Breadth-first Search

import collections

#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m==0: return -1
        n = len(grid[0])
        count = collections.defaultdict(int)
        maxCnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, count)
                    maxCnt += 1
        ans = float('inf')
        for i,j in count:
            if count[(i,j)] == maxCnt:
                ans = min(ans, -grid[i][j])
        return -1 if ans==float('inf') else ans

    def bfs(self, grid, i, j, count):
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        queue.append((i,j))
        visited = set()
        visited.add((i,j))
        dist = 0
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        while queue:
            dist += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for k in range(4):
                    ni = i+dx[k]
                    nj = j+dy[k]
                    if ni<0 or ni>=m or nj<0 or nj>=n or grid[ni][nj]>0 or (ni, nj) in visited: continue
                    queue.append((ni, nj))
                    visited.add((ni, nj))
                    grid[ni][nj] -= dist
                    count[(ni,nj)] += 1



        
        
#leetcode submit region end(Prohibit modification and deletion)
