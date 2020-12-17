#You are given a m x n 2D grid initialized with these three possible values. 
#
# 
# -1 - A wall or an obstacle. 
# 0 - A gate. 
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647. 
# 
#
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF. 
#
# Example: 
#
# Given the 2D grid: 
#
# 
#INF  -1  0  INF
#INF INF INF  -1
#INF  -1 INF  -1
#  0  -1 INF INF
# 
#
# After running your function, the 2D grid should be: 
#
# 
#  3  -1   0   1
#  2   2   1  -1
#  1  -1   2  -1
#  0  -1   3   4
# 
# Related Topics Breadth-first Search


import collections
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if m==0: return
        n = len(rooms[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        level = 0
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        while queue:
            level += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for k in range(4):
                    ni = i+dx[k]
                    nj = j+dy[k]
                    if ni<0 or ni>=m or nj<0 or nj>=n  or rooms[ni][nj]<level: continue
                    rooms[ni][nj] = level
                    queue.append((ni, nj))
#leetcode submit region end(Prohibit modification and deletion)
