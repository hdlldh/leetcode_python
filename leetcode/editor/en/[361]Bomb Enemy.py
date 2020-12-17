#Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb. 
#The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed. 
#Note: You can only put the bomb at an empty cell. 
#
# Example: 
#
# 
# 
#Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
#Output: 3 
#Explanation: For the given grid,
#
#0 E 0 0 
#E 0 W E 
#0 E 0 0
#
#Placing a bomb at (1,1) kills 3 enemies.
# 
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        m = len(grid)
        if m==0: return 0
        n = len(grid[0])
        v1 = [[0] * n for _ in range(m)]
        v2 = [[0] * n for _ in range(m)]
        v3 = [[0] * n for _ in range(m)]
        v4 = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(1, n):
                if grid[i][j-1]=='W': continue
                if grid[i][j-1]=='E':v1[i][j] = v1[i][j-1]+1
                else: v1[i][j] = v1[i][j-1]
            for j in range(n-2, -1, -1):
                if grid[i][j+1]=='W':continue
                if grid[i][j+1]=='E': v2[i][j] = v2[i][j+1]+1
                else: v2[i][j] = v2[i][j+1]

        for j in range(n):
            for i in range(1, m):
                if grid[i-1][j]=='W': continue
                if grid[i-1][j]=='E':v3[i][j] = v3[i-1][j]+1
                else: v3[i][j] = v3[i-1][j]
            for i in range(m-2, -1, -1):
                if grid[i+1][j]=='W':continue
                if grid[i+1][j]=='E': v4[i][j] = v4[i+1][j]+1
                else: v4[i][j] = v4[i+1][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    ans = max(ans, v1[i][j]+v2[i][j]+v3[i][j]+v4[i][j])
        return ans

#leetcode submit region end(Prohibit modification and deletion)
