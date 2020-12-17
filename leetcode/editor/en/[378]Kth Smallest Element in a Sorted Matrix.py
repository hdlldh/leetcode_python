#Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix. 
#
# 
#Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# 
#
# Example:
# 
#matrix = [
#   [ 1,  5,  9],
#   [10, 11, 13],
#   [12, 13, 15]
#],
#k = 8,
#
#return 13.
# 
# 
#
# Note: 
#You may assume k is always valid, 1 ≤ k ≤ n2. Related Topics Binary Search Heap



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        low = matrix[0][0]
        high = matrix[m-1][m-1]
        while low<=high:
            mid = low + (high-low)//2
            cnt = self.count(matrix, mid)
            if cnt >= k: high = mid -1
            else: low = mid +1
        return low

    def count(self, matrix, target):
        m = len(matrix)
        row = 0
        col = m-1
        cnt = 0
        while row<m and col>=0:
            if matrix[row][col]<=target:
                cnt += col+1
                row += 1
            else:
                col -= 1
        return cnt
#leetcode submit region end(Prohibit modification and deletion)
