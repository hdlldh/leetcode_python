# You are given a map in form of a two-dimensional integer grid where 1 represen
# ts land and 0 represents water. 
# 
#  Grid cells are connected horizontally/vertically (not diagonally). The grid i
# s completely surrounded by water, and there is exactly one island (i.e., one or 
# more connected land cells). 
# 
#  The island doesn't have "lakes" (water inside that isn't connected to the wat
# er around the island). One cell is a square with side length 1. The grid is rect
# angular, width and height don't exceed 100. Determine the perimeter of the islan
# d. 
# 
#  
# 
#  Example: 
# 
#  
# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# 
# Output: 16
# 
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
#  
#  Related Topics Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
# leetcode submit region end(Prohibit modification and deletion)
