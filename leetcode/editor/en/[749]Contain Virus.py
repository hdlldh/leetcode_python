#
#A virus is spreading rapidly, and your task is to quarantine the infected area 
#by installing walls.
# 
#The world is modeled as a 2-D array of cells, where 0 represents uninfected cel
#ls, and 1 represents cells contaminated with the virus. A wall (and only one wal
#l) can be installed between any two 4-directionally adjacent cells, on the share
#d boundary.
# 
#Every night, the virus spreads to all neighboring cells in all four directions 
#unless blocked by a wall.
#Resources are limited. Each day, you can install walls around only one region -
#- the affected area (continuous block of infected cells) that threatens the most
# uninfected cells the following night. There will never be a tie.
# 
#Can you save the day? If so, what is the number of walls required? If not, and 
#the world becomes fully infected, return the number of walls used.
# 
#
# Example 1: 
# 
#Input: grid = 
#[[0,1,0,0,0,0,0,1],
# [0,1,0,0,0,0,0,1],
# [0,0,0,0,0,0,0,1],
# [0,0,0,0,0,0,0,0]]
#Output: 10
#Explanation:
#There are 2 contaminated regions.
#On the first day, add 5 walls to quarantine the viral region on the left. The b
#oard after the virus spreads is:
#
#[[0,1,0,0,0,0,1,1],
# [0,1,0,0,0,0,1,1],
# [0,0,0,0,0,0,1,1],
# [0,0,0,0,0,0,0,1]]
#
#On the second day, add 5 walls to quarantine the viral region on the right. The
# virus is fully contained.
# 
# 
#
# Example 2: 
# 
#Input: grid = 
#[[1,1,1],
# [1,0,1],
# [1,1,1]]
#Output: 4
#Explanation: Even though there is only one cell saved, there are 4 walls built.
#
#Notice that walls are only built on the shared boundary of two different cells.
#
# 
# 
#
# Example 3: 
# 
#Input: grid = 
#[[1,1,1,0,0,0,0,0,0],
# [1,0,1,0,1,1,1,1,1],
# [1,1,1,0,0,0,0,0,0]]
#Output: 13
#Explanation: The region on the left only builds two new walls.
# 
# 
#
# Note: 
# 
# The number of rows and columns of grid will each be in the range [1, 50]. 
# Each grid[i][j] will be either 0 or 1. 
# Throughout the described process, there is always a contiguous viral region th
#at will infect strictly more uncontaminated squares in the next round. 
# 
# Related Topics Depth-first Search




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ans = 0
        while True:
            walls = collections.defaultdict(int)
            affect = collections.defaultdict(set)
            next = collections.defaultdict(set)
            visited = [[False] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        self.dfs(grid, i, j, i, j, walls, affect, next, visited)

            if not next: break
            max_affect = -1
            max_p = None
            for p in next.keys():
                if len(next[p]) > max_affect:
                    max_p = p
                    max_affect = len(next[p])

            ans += walls[max_p]
            for p in affect[max_p]:
                grid[p[0]][p[1]] = 2

            for p in next.keys():
                if p == max_p: continue
                for p1 in next[p]:
                    grid[p1[0]][p1[1]] = 1

        return ans



    def dfs(self, grid, i, j, i0, j0, walls, affect, next, visited):
        m, n = len(grid), len(grid[0])
        if i<0 or i>=m or j<0 or j>=n: return
        if grid[i][j] == 0:
            next[(i0, j0)].add((i, j))
            walls[(i0, j0)] += 1
            return
        if not visited[i][j] and grid[i][j] == 1:
            affect[(i0, j0)].add((i, j))
            visited[i][j] = True
            self.dfs(grid, i + 1, j, i0, j0, walls, affect, next, visited)
            self.dfs(grid, i - 1, j, i0, j0, walls, affect, next, visited)
            self.dfs(grid, i, j + 1, i0, j0, walls, affect, next, visited)
            self.dfs(grid, i, j - 1, i0, j0, walls, affect, next, visited)
        return

        
#leetcode submit region end(Prohibit modification and deletion)
