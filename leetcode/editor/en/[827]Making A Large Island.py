#In a 2D grid of 0s and 1s, we change at most one 0 to a 1. 
#
# After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s). 
#
# Example 1: 
#
# 
#Input: [[1, 0], [0, 1]]
#Output: 3
#Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# 
#
# Example 2: 
#
# 
#Input: [[1, 1], [1, 0]]
#Output: 4
#Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4. 
#
# Example 3: 
#
# 
#Input: [[1, 1], [1, 1]]
#Output: 4
#Explanation: Can't change any 0 to 1, only one island with area = 4. 
#
# 
#
# Notes: 
#
# 
# 1 <= grid.length = grid[0].length <= 50. 
# 0 <= grid[i][j] <= 1. 
# 
#
# 
# Related Topics Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ans = 0
        color = 2
        areas ={}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[color] = self.getArea(grid, i, j, color)
                    ans = max(ans, areas[color])
                    color += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] ==0:
                    nei = set()
                    if i>0: nei.add(grid[i-1][j])
                    if j>0: nei.add(grid[i][j-1])
                    if i<m-1: nei.add(grid[i+1][j])
                    if j<n-1: nei.add(grid[i][j+1])
                    area = 1
                    for color in nei:
                        if color>1: area += areas[color]
                    ans = max(ans, area)
        return ans

    def getArea(self, grid, i, j, color):
        m, n = len(grid), len(grid[0])
        if i<0 or i>=m or j<0 or j>=n: return 0
        if grid[i][j] != 1: return 0
        grid[i][j] = color
        ans = 1
        di = [0, -1, 0, 1]
        dj = [-1, 0, 1, 0]
        for k in range(4):
            ans += self.getArea(grid, i+di[k], j+dj[k], color)
        return ans
#leetcode submit region end(Prohibit modification and deletion)
