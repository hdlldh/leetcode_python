# In an N by N square grid, each cell is either empty (0) or blocked (1). 
# 
#  A clear path from top-left to bottom-right has length k if and only if it is 
# composed of cells C_1, C_2, ..., C_k such that: 
# 
#  
#  Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are d
# ifferent and share an edge or corner) 
#  C_1 is at location (0, 0) (ie. has value grid[0][0]) 
#  C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1]) 
#  If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0). 
# 
#  
# 
#  Return the length of the shortest such clear path from top-left to bottom-rig
# ht. If such a path does not exist, return -1. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [[0,1],[1,0]]
# 
# 
# Output: 2
# 
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [[0,0,0],[1,1,0],[1,1,0]]
# 
# 
# Output: 4
# 
#  
# 
#  
#  
# 
#  Note: 
# 
#  
#  1 <= grid.length == grid[0].length <= 100 
#  grid[r][c] is 0 or 1 
#  
#  Related Topics Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1: return -1
        queue = collections.deque()
        queue.append([0, 0])
        visited = [[0] * n for _ in range(m)]
        visited[0][0] = 1
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                ux, uy = queue.popleft()
                if ux == m - 1 and uy == n - 1: return steps + 1
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0: continue
                        vx = ux + dx
                        vy = uy + dy
                        if vx < 0 or vx >= m or vy < 0 or vy >= n: continue
                        if grid[vx][vy] == 1 or visited[vx][vy] == 1: continue
                        queue.append([vx, vy])
                        visited[vx][vy] = 1
            steps += 1
        return -1
# leetcode submit region end(Prohibit modification and deletion)
