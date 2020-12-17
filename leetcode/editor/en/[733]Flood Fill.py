# 
# An image is represented by a 2-D array of integers, each integer representing 
# the pixel value of the image (from 0 to 65535).
#  
# Given a coordinate (sr, sc) representing the starting pixel (row and column) o
# f the flood fill, and a pixel value newColor, "flood fill" the image.
#  
# To perform a "flood fill", consider the starting pixel, plus any pixels connec
# ted 4-directionally to the starting pixel of the same color as the starting pixe
# l, plus any pixels connected 4-directionally to those pixels (also with the same
#  color as the starting pixel), and so on. Replace the color of all of the aforem
# entioned pixels with the newColor.
#  
# At the end, return the modified image.
#  
#  Example 1: 
#  
# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels con
# nected 
# by a path of the same color as the starting pixel are colored with the new col
# or.
# Note the bottom corner is not colored 2, because it is not 4-directionally con
# nected
# to the starting pixel.
#  
#  
# 
#  Note:
#  The length of image and image[0] will be in the range [1, 50]. 
#  The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < im
# age[0].length. 
#  The value of each color in image[i][j] and newColor will be an integer in [0,
#  65535]. 
#  Related Topics Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]
        visited = set()

        def dfs(image, i, j, oldColor, newColor, visited):
            if (i, j) in visited: return
            visited.add((i, j))
            if image[i][j] != oldColor: return
            image[i][j] = newColor
            if i > 0: dfs(image, i - 1, j, oldColor, newColor, visited)
            if j > 0: dfs(image, i, j - 1, oldColor, newColor, visited)
            if i < len(image) - 1: dfs(image, i + 1, j, oldColor, newColor, visited)
            if j < len(image[0]) - 1: dfs(image, i, j + 1, oldColor, newColor, visited)

        dfs(image, sr, sc, oldColor, newColor, visited)

        return image
        
# leetcode submit region end(Prohibit modification and deletion)
