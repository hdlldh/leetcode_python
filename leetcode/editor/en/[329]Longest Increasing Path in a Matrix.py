#Given an integer matrix, find the length of the longest increasing path. 
#
# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed). 
#
# Example 1: 
#
# 
#Input: nums = 
#[
#  [9,9,4],
#  [6,6,8],
#  [2,1,1]
#] 
#Output: 4 
#Explanation: The longest increasing path is [1, 2, 6, 9].
# 
#
# Example 2: 
#
# 
#Input: nums = 
#[
#  [3,4,5],
#  [3,2,6],
#  [2,2,1]
#] 
#Output: 4 
#Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# 
# Related Topics Depth-first Search Topological Sort Memoization



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        ans = 0
        if m==0: return ans
        n = len(matrix[0])
        mem = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(matrix, i, j, mem))
        return ans

    def dfs(self, matrix, i, j, mem):
        if mem[i][j] >0 : return mem[i][j]
        m, n = len(matrix), len(matrix[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        mem[i][j] = 1
        for k in range(4):
            ni = i+dx[k]
            nj = j+dy[k]
            if ni<0 or ni>=m or nj<0 or nj>=n: continue
            if matrix[ni][nj] > matrix[i][j]:
                mem[i][j] = max(mem[i][j], self.dfs(matrix, ni, nj, mem)+1)
        return mem[i][j]
#leetcode submit region end(Prohibit modification and deletion)
