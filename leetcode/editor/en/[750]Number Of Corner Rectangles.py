#Given a grid where each entry is only 0 or 1, find the number of corner rectang
#les. 
#
# A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rect
#angle. Note that only the corners need to have the value 1. Also, all four 1s us
#ed must be distinct. 
#
# 
#
# Example 1: 
#
# 
#Input: grid = 
#[[1, 0, 0, 1, 0],
# [0, 0, 1, 0, 1],
# [0, 0, 0, 1, 0],
# [1, 0, 1, 0, 1]]
#Output: 1
#Explanation: There is only one corner rectangle, with corners grid[1][2], grid[
#1][4], grid[3][2], grid[3][4].
# 
#
# 
#
# Example 2: 
#
# 
#Input: grid = 
#[[1, 1, 1],
# [1, 1, 1],
# [1, 1, 1]]
#Output: 9
#Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and on
#e 3x3 rectangle.
# 
#
# 
#
# Example 3: 
#
# 
#Input: grid = 
#[[1, 1, 1, 1]]
#Output: 0
#Explanation: Rectangles must have four distinct corners.
# 
#
# 
#
# Note: 
#
# 
# The number of rows and columns of grid will each be in the range [1, 200]. 
# Each grid[i][j] will be either 0 or 1. 
# The number of 1s in the grid will be at most 6000. 
# 
#
# 
# Related Topics Dynamic Programming




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n= len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            ones = []
            for k in range(n):
                if grid[i][k]==1: ones.append(k)
            for j in range(i+1, m):
                cnt = 0
                for k in ones:
                    if (grid[j][k]==1): cnt+=1
                ans += cnt*(cnt-1)//2
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
