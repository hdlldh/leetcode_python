#We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is 
#the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks. 
#
# We start at the starting point, and one move consists of walking one space in 
#one of the 4 cardinal directions. We cannot walk outside the grid, or walk into 
#a wall. If we walk over a key, we pick it up. We can't walk over a lock unless w
#e have the corresponding key. 
#
# For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter 
#of the first K letters of the English alphabet in the grid. This means that ther
#e is exactly one key for each lock, and one lock for each key; and also that the
# letters used to represent the keys and locks were chosen in the same order as t
#he English alphabet. 
#
# Return the lowest number of moves to acquire all keys. If it's impossible, ret
#urn -1. 
#
# 
#
# 
# Example 1: 
#
# 
#Input: ["@.a.#","###.#","b.A.B"]
#Output: 8
# 
#
# 
# Example 2: 
#
# 
#Input: ["@..aA","..B#.","....b"]
#Output: 6
# 
# 
#
# 
#
# Note: 
#
# 
# 1 <= grid.length <= 30 
# 1 <= grid[0].length <= 30 
# grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F' 
# The number of keys is in [1, 6]. Each key has a different letter and opens exa
#ctly one lock. 
# 
# 
# Related Topics Heap Breadth-first Search




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        seen = set()
        allKey = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@':
                    queue.append((i, j, 0))
                    seen.add((i, j, 0))
                elif 'f'>=grid[i][j]>='a':
                    allKey |= 1<<(ord(grid[i][j])-ord('a'))
        steps = 0
        dirs = [-1, 0, 1, 0, -1]
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j, s = queue.popleft()
                if s == allKey: return steps
                for k in range(4):
                    ti = i+dirs[k]
                    tj = j+dirs[k+1]
                    if ti<0 or ti>=m or tj<0 or tj>=n: continue
                    if grid[ti][tj]=='#': continue
                    if 'F'>=grid[ti][tj]>='A' and (s & (1<<(ord(grid[ti][tj])-ord('A'))))==0: continue
                    if 'f' >= grid[ti][tj] >= 'a': ts = s | 1<<(ord(grid[ti][tj])-ord('a'))
                    else: ts = s
                    if (ti, tj, ts) in seen: continue
                    queue.append((ti, tj, ts))
                    seen.add((ti, tj, ts))
            steps+=1
        return -1
#leetcode submit region end(Prohibit modification and deletion)
