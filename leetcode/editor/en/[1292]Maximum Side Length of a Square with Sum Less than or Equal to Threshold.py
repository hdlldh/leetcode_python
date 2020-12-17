# Given a m x n matrix mat and an integer threshold. Return the maximum side-len
# gth of a square with a sum less than or equal to threshold or return 0 if there 
# is no such square. 
# 
#  
#  Example 1: 
# 
#  
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as sh
# own.
#  
# 
#  Example 2: 
# 
#  
# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], th
# reshold = 1
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
# Output: 3
#  
# 
#  Example 4: 
# 
#  
# Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], thresho
# ld = 40184
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= m, n <= 300 
#  m == mat.length 
#  n == mat[i].length 
#  0 <= mat[i][j] <= 10000 
#  0 <= threshold <= 10^5 
#  
#  Related Topics Array Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m = len(mat)
        if m == 0: return 0
        n = len(mat[0])

        low = 1
        high = min(m, n)

        psum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                psum[i + 1][j + 1] = psum[i][j + 1] + psum[i + 1][j] - psum[i][j] + mat[i][j]
        print(psum)

        while low <= high:
            mid = low + (high - low) // 2
            if not self.check(psum, mid, threshold):
                high = mid - 1
            else:
                low = mid + 1
        return high

    def check(self, psum, l, threshold):
        for i in xrange(len(psum) - l):
            for j in xrange(len(psum[0]) - l):
                s = psum[i + l][j + l] - psum[i + l][j] - psum[i][j + l] + psum[i][j]
                if s <= threshold: return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
