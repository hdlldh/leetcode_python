#A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. 
#
# Example: 
#
# 
#Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
#Output: [1,1,2,3]
# 
#
# Explanation: 
#
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land). 
#
# 
#0 0 0
#0 0 0
#0 0 0
# 
#
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. 
#
# 
#1 0 0
#0 0 0   Number of islands = 1
#0 0 0
# 
#
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. 
#
# 
#1 1 0
#0 0 0   Number of islands = 1
#0 0 0
# 
#
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. 
#
# 
#1 1 0
#0 0 1   Number of islands = 2
#0 0 0
# 
#
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. 
#
# 
#1 1 0
#0 0 1   Number of islands = 3
#0 1 0
# 
#
# Follow up: 
#
# Can you do it in time complexity O(k log mn), where k is the length of the positions? 
# Related Topics Union Find



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent = [-1] * (m * n)
        size = [0] * (m * n)
        filled = set()
        ans = []
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        count = 0

        def add(parent, size, i):
            parent[i] = i
            size[i] += 1

        def find(parent, i):
            if parent[i] != i:
                return find(parent, parent[i])
            return i

        def union(parent, size, i, j):
            root_i = find(parent, i)
            root_j = find(parent, j)

            if size[root_i] >= size[root_j]:
                parent[root_j] = root_i
                size[root_i] += size[root_j]
            else:
                parent[root_i] = root_j
                size[root_j] += size[root_i]
            return

        for pos in positions:
            index = pos[0] * n + pos[1]
            add(parent, size, index)
            if (pos[0], pos[1]) in filled:
                ans.append(count)
                continue
            filled.add((pos[0], pos[1]))
            count += 1

            for d in directions:
                i = pos[0] + d[0]
                j = pos[1] + d[1]
                if i < 0 or i >= m: continue
                if j < 0 or j >= n: continue
                if (i, j) not in filled: continue
                if find(parent, i * n + j) != find(parent, index):
                    union(parent, size, i * n + j, index)
                    count -= 1
            ans.append(count)
        return ans
#leetcode submit region end(Prohibit modification and deletion)
