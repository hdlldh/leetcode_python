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
#update(3, 2, 2)
#sumRegion(2, 1, 4, 3) -> 10
# 
# 
#
# Note: 
# 
# The matrix is only modifiable by the update function. 
# You may assume the number of calls to update and sumRegion function is distributed evenly. 
# You may assume that row1 ≤ row2 and col1 ≤ col2. 
# 
# Related Topics Binary Indexed Tree Segment Tree



#leetcode submit region begin(Prohibit modification and deletion)
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m = len(matrix)
        if self.m == 0: return
        self.n = len(matrix[0])
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        self.matrix = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & -j
            i += i & -i

    def query(self, row, col):
        s = 0
        i = row + 1

        while i > 0:
            j = col + 1
            while j > 0:
                s += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return s

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.query(row2, col2)
        elif row1 == 0:
            return self.query(row2, col2) - self.query(row2, col1 - 1)
        elif col1 == 0:
            return self.query(row2, col2) - self.query(row1 - 1, col2)
        else:
            return self.query(row2, col2) - self.query(row2, col1 - 1) - self.query(row1 - 1, col2) + self.query(row1 - 1, col1 - 1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
#leetcode submit region end(Prohibit modification and deletion)
