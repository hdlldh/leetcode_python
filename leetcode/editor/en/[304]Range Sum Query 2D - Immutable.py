#Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2). 
#
# 
# 
#The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
# 
#
# Example: 
# 
#Given matrix = [
#  [3, 0, 1, 4, 2],
#  [5, 6, 3, 2, 1],
#  [1, 2, 0, 1, 5],
#  [4, 1, 0, 1, 7],
#  [1, 0, 3, 0, 5]
#]
#
#sumRegion(2, 1, 4, 3) -> 8
#sumRegion(1, 1, 2, 2) -> 11
#sumRegion(1, 2, 2, 4) -> 12
# 
# 
#
# Note: 
# 
# You may assume that the matrix does not change. 
# There are many calls to sumRegion function. 
# You may assume that row1 ≤ row2 and col1 ≤ col2. 
# 
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m==0: return
        n = len(matrix[0])
        self.data = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.data[i+1][j+1] = self.data[i+1][j] + self.data[i][j+1]+ matrix[i][j] -self.data[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.data[row2+1][col2+1]-self.data[row2+1][col1]-self.data[row1][col2+1]+self.data[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
#leetcode submit region end(Prohibit modification and deletion)
