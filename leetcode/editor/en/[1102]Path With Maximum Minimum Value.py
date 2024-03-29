#Given a matrix of integers A with R rows and C columns, find the maximum score 
#of a path starting at [0,0] and ending at [R-1,C-1]. 
#
# The score of a path is the minimum value in that path. For example, the value 
#of the path 8 → 4 → 5 → 9 is 4. 
#
# A path moves some number of times from one visited cell to any neighbouring un
#visited cell in one of the 4 cardinal directions (north, east, west, south). 
#
# 
#
# Example 1: 
#
# 
#
# 
#Input: [[5,4,5],[1,2,6],[7,4,6]]
#Output: 4
#Explanation: 
#The path with the maximum score is highlighted in yellow. 
# 
#
# Example 2: 
#
# 
#
# 
#Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
#Output: 2 
#
# Example 3: 
#
# 
#
# 
#Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]
#]
#Output: 3 
#
# 
#
# Note: 
#
# 
# 1 <= R, C <= 100 
# 0 <= A[i][j] <= 10^9 
# 
# Related Topics Depth-first Search Union Find Graph




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        pq = [[-A[0][0], 0, 0]]
        seen = [[0]*n for _ in range(m)]
        ans = A[0][0]
        dirs = [-1, 0, 1, 0, -1]
        while pq:
            u, i, j = heapq.heappop(pq)
            if seen[i][j] == 1: continue
            seen[i][j] = 1
            ans = min(ans, -u)
            if i==m-1 and j==n-1: return ans
            for k in range(4):
                ti = i+dirs[k]
                tj = j+dirs[k+1]
                if ti<0 or ti>=m or tj<0 or tj>=n: continue
                heapq.heappush(pq, [-A[ti][tj], ti, tj])
        return ans

        
#leetcode submit region end(Prohibit modification and deletion)
