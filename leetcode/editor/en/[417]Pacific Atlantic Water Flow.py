#Given an m x n matrix of non-negative integers representing the height of each 
#unit cell in a continent, the "Pacific ocean" touches the left and top edges of 
#the matrix and the "Atlantic ocean" touches the right and bottom edges. 
#
# Water can only flow in four directions (up, down, left, or right) from a cell 
#to another one with height equal or lower. 
#
# Find the list of grid coordinates where water can flow to both the Pacific and
# Atlantic ocean. 
#
# Note: 
#
# 
# The order of returned grid coordinates does not matter. 
# Both m and n are less than 150. 
# 
#
# 
#
# Example: 
#
# 
#Given the following 5x5 matrix:
#
#  Pacific ~   ~   ~   ~   ~ 
#       ~  1   2   2   3  (5) *
#       ~  3   2   3  (4) (4) *
#       ~  2   4  (5)  3   1  *
#       ~ (6) (7)  1   4   5  *
#       ~ (5)  1   1   2   4  *
#          *   *   *   *   * Atlantic
#
#Return:
#
#[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parent
#heses in above matrix).
# 
#
# 
# Related Topics Depth-first Search Breadth-first Search




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        m = len(matrix)
        if m == 0: return ans
        n = len(matrix[0])
        pac_queue = collections.deque()
        pac_visited = set()
        for i in range(m):
            pac_queue.append([i, 0])
            pac_visited.add((i, 0))
        for j in range(n):
            pac_queue.append([0, j])
            pac_visited.add((0, j))
        self.helper(matrix, pac_queue, pac_visited)

        ant_queue = collections.deque()
        ant_visited = set()
        for i in range(m):
            ant_queue.append([i, n-1])
            ant_visited.add((i, n-1))
        for j in range(n):
            ant_queue.append([m-1, j])
            ant_visited.add((m-1, j))
        self.helper(matrix, ant_queue, ant_visited)

        for x, y in pac_visited:
            if (x, y) in ant_visited: ans.append([x, y])
        return ans

    def helper(self,matrix, queue, visited):
        m, n = len(matrix), len(matrix[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                tx = x + dx[k]
                ty = y + dy[k]
                if tx < 0 or tx >= m or ty < 0 or ty >= n: continue
                if matrix[tx][ty] < matrix[x][y] or (tx, ty) in visited: continue
                queue.append([tx, ty])
                visited.add((tx, ty))
#leetcode submit region end(Prohibit modification and deletion)
