#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. 
#
# Example 1: 
#
# 
#Input:
#11110
#11010
#11000
#00000
#
#Output: 1
# 
#
# Example 2: 
#
# 
#Input:
#11000
#11000
#00100
#00011
#
#Output: 3
# Related Topics Depth-first Search Breadth-first Search Union Find



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m==0: return 0
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    ans += 1
        return ans

    def dfs(self, board, i, j):
        m, n = len(board), len(board[0])
        if i<0 or i>=m or j<0 or j>=n: return
        if board[i][j]!='1': return
        board[i][j] = '#'
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        for k in range(4):
            self.dfs(board, i+dx[k], j+dy[k])
        
#leetcode submit region end(Prohibit modification and deletion)
