# We have a grid of 1s and 0s; the 1s in a cell represent bricks. A brick will n
# ot drop if and only if it is directly connected to the top of the grid, or at le
# ast one of its (4-way) adjacent bricks will not drop. 
# 
#  We will do some erasures sequentially. Each time we want to do the erasure at
#  the location (i, j), the brick (if it exists) on that location will disappear, 
# and then some other bricks may drop because of that erasure. 
# 
#  Return an array representing the number of bricks that will drop after each e
# rasure in sequence. 
# 
#  
# Example 1:
# Input: 
# grid = [[1,0,0,0],[1,1,1,0]]
# hits = [[1,0]]
# Output: [2]
# Explanation: 
# If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So 
# we should return 2. 
# 
#  
# Example 2:
# Input: 
# grid = [[1,0,0,0],[1,1,0,0]]
# hits = [[1,1],[1,0]]
# Output: [0,0]
# Explanation: 
# When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared
#  due to the last move. So each erasure will cause no bricks dropping.  Note that
#  the erased brick (1, 0) will not be counted as a dropped brick. 
# 
#  
# 
#  Note: 
# 
#  
#  The number of rows and columns in the grid will be in the range [1, 200]. 
#  The number of erasures will not exceed the area of the grid. 
#  It is guaranteed that each erasure will be different from any other erasure, 
# and located inside the grid. 
#  An erasure may refer to a location with no brick - if it does, no bricks drop
# . 
#  
#  Related Topics Union Find


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        for i, j in hits: grid[i][j] -= 1

        roots = [i for i in range(m*n)]
        for j in range(n):
            if grid[0][j] == 1: roots[j] = -1

        def find(roots, x):
            while roots[x] != x:
                x = roots[x]
            return x

        def union(root, x, y):
        
# leetcode submit region end(Prohibit modification and deletion)
