#On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j). 
#
# Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim. 
#
# You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)? 
#
# Example 1: 
#
# 
#Input: [[0,2],[1,3]]
#Output: 3
#Explanation:
#At time 0, you are in grid location (0, 0).
#You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
#
#You cannot reach point (1, 1) until time 3.
#When the depth of water is 3, we can swim anywhere inside the grid.
# 
#
# Example 2: 
#
# 
#Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
#Output: 16
#Explanation:
# 0  1  2  3  4
#24 23 22 21  5
#12 13 14 15 16
#11 17 18 19 20
#10  9  8  7  6
#
#The final route is marked in bold.
#We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
# 
#
# Note: 
#
# 
# 2 <= N <= 50. 
# grid[i][j] is a permutation of [0, ..., N*N - 1]. 
# 
# Related Topics Binary Search Heap Depth-first Search Union Find



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def swimInWater2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        while pq:
            u, x, y = heapq.heappop(pq)
            if x==n-1 and y==n-1: return u
            for k in range(4):
                tx = x+dx[k]
                ty = y+dy[k]
                if tx<0 or tx>=n or ty<0 or ty>=n or (tx, ty) in visited: continue
                v = max(u, grid[tx][ty])
                heapq.heappush(pq, (v, tx, ty))
                visited.add((tx, ty))

    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        def bfs(grid, target):
            queue = collections.deque()
            queue.append((0, 0))
            visited = set()
            visited.add((0, 0))
            while queue:
                x, y = queue.popleft()
                if x==n-1 and y==n-1: return True
                for k in range(4):
                    tx = x + dx[k]
                    ty = y + dy[k]
                    if tx < 0 or tx >= n or ty < 0 or ty >= n or grid[tx][ty] > target or (tx, ty) in visited:continue
                    queue.append((tx, ty))
                    visited.add((tx, ty))
            return False
        low = grid[0][0]
        high = n*n-1
        while low<=high:
            mid = low + (high-low)//2
            if bfs(grid, mid): high = mid -1
            else: low = mid +1
        return low

#leetcode submit region end(Prohibit modification and deletion)
