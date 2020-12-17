# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (r
# epresenting land) connected 4-directionally (horizontal or vertical.) You may as
# sume all four edges of the grid are surrounded by water. 
# 
#  Count the number of distinct islands. An island is considered to be the same 
# as another if they have the same shape, or have the same shape after rotation (9
# 0, 180, or 270 degrees only) or reflection (left/right direction or up/down dire
# ction). 
# 
#  Example 1: 
#  
# 11000
# 10000
# 00001
# 00011
#  
# Given the above grid map, return 1.
#  
# Notice that:
#  
# 11
# 1
#  
# and
#  
#  1
# 11
#  
# are considered same island shapes. Because if we make a 180 degrees clockwise 
# rotation on the first island, then two islands will have the same shapes.
#  
# 
#  Example 2: 
#  
# 11100
# 10001
# 01001
# 01110 
# Given the above grid map, return 2. 
#  
# Here are the two distinct islands:
#  
# 111
# 1
#  
# and
#  
# 1
# 1
#  
#  
# Notice that:
#  
# 111
# 1
#  
# and
#  
# 1
# 111
#  
# are considered same island shapes. Because if we flip the first array in the u
# p/down direction, then they have the same shapes.
#  
# 
#  Note:
# The length of each dimension in the given grid does not exceed 50.
#  Related Topics Hash Table Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        seen = [[0] * n for _ in range(m)]
        ans = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and seen[i][j] != 1:
                    shape = []
                    self.dfs(grid, seen, i, j, shape)
                    shape = self.normalize(shape)
                    ans.add(tuple([tuple(p) for p in shape]))
        return len(ans)

    def dfs(self, grid, seen, i, j, shape):
        m, n = len(grid), len(grid[0])
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0 or seen[i][j]==1: return
        shape.append([i, j])
        seen[i][j] =1
        dirs = [-1, 0, 1, 0, -1]
        for k in range(4):
            self.dfs(grid, seen, i+dirs[k], j+dirs[k+1], shape)

    def normalize(self, shape):
        shapes = [[] for _ in range(8)]
        for x, y in shape:
            shapes[0].append([x, y])
            shapes[1].append([-x, y])
            shapes[2].append([x, -y])
            shapes[3].append([-x, -y])
            shapes[4].append([y, x])
            shapes[5].append([-y, x])
            shapes[6].append([y, -x])
            shapes[7].append([-y, -x])
        for shape in shapes:
            shape.sort()
            for i in range(len(shape)-1, -1, -1):
                shape[i][0] -= shape[0][0]
                shape[i][1] -= shape[0][1]
        shapes.sort()
        return shapes[0]
        
# leetcode submit region end(Prohibit modification and deletion)
