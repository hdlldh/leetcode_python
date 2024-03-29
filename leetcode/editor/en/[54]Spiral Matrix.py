#Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order. 
#
# Example 1: 
#
# 
#Input:
#[
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
#]
#Output: [1,2,3,6,9,8,7,4,5]
# 
#
# Example 2: 
# 
#Input:
#[
#  [1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9,10,11,12]
#]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# Related Topics Array



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        m = len(matrix)
        if m==0: return ans
        n = len(matrix[0])
        left, right = 0, n-1
        top, bottom = 0, m-1
        while True:
            for j in range(left, right+1): ans.append(matrix[top][j])
            top += 1
            if top>bottom: break
            for i in range(top, bottom+1): ans.append(matrix[i][right])
            right -= 1
            if left>right:break
            for j in range(right, left-1, -1): ans.append(matrix[bottom][j])
            bottom -= 1
            if top>bottom: break
            for i in range(bottom, top-1, -1): ans.append(matrix[i][left])
            left += 1
            if left>right:break
        return ans
#leetcode submit region end(Prohibit modification and deletion)
