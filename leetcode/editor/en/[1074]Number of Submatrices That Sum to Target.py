# Given a matrix, and a target, return the number of non-empty submatrices that 
# sum to target. 
# 
#  A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x 
# <= x2 and y1 <= y <= y2. 
# 
#  Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if th
# ey have some coordinate that is different: for example, if x1 != x1'. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2
# x2 submatrix.
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= matrix.length <= 300 
#  1 <= matrix[0].length <= 300 
#  -1000 <= matrix[i] <= 1000 
#  -10^8 <= target <= 10^8 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= matrix.length <= 100 
#  1 <= matrix[0].length <= 100 
#  -1000 <= matrix[i] <= 1000 
#  -10^8 <= target <= 10^8 
#  
#  Related Topics Array Dynamic Programming Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        psum = [[0] * (n+1) for _ in range(m+1)]
        ans = 0

        for i in range(1,m+1):
            for j in range(1, n+1):
                psum[i][j] = psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1] + matrix[i-1][j-1]
        #print(psum)

        for i in range(m):
            for j in range(i+1):
                count = collections.defaultdict(int)
                for k in range(n):
                    s = psum[i+1][k+1] - psum[j][k+1]
                    #print(i, j, k, s)
                    if s == target: ans +=1
                    if s - target in count: ans += count[s-target]
                    count[s] += 1
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)
