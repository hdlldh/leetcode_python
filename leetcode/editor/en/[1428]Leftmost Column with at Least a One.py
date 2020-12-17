# (This problem is an interactive problem.) 
# 
#  A binary matrix means that all elements are 0 or 1. For each individual row o
# f the matrix, this row is sorted in non-decreasing order. 
# 
#  Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0
# -indexed) with at least a 1 in it. If such index doesn't exist, return -1. 
# 
#  You can't access the Binary Matrix directly. You may only access the matrix u
# sing a BinaryMatrix interface: 
# 
#  
#  BinaryMatrix.get(row, col) returns the element of the matrix at index (row, c
# ol) (0-indexed). 
#  BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which me
# ans the matrix is rows * cols. 
#  
# 
#  Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wr
# ong Answer. Also, any solutions that attempt to circumvent the judge will result
#  in disqualification. 
# 
#  For custom testing purposes you're given the binary matrix mat as input in th
# e following four examples. You will not have access the binary matrix directly. 
# 
# 
#  
# 
#  
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: mat = [[0,0],[1,1]]
# Output: 0
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: mat = [[0,0],[0,1]]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# 
#  
# Input: mat = [[0,0],[0,0]]
# Output: -1 
# 
#  Example 4: 
# 
#  
# 
#  
# Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  rows == mat.length 
#  cols == mat[i].length 
#  1 <= rows, cols <= 100 
#  mat[i][j] is either 0 or 1. 
#  mat[i] is sorted in a non-decreasing way. 
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
# leetcode submit region end(Prohibit modification and deletion)
