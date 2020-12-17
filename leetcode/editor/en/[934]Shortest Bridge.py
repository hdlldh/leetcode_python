#In a given 2D binary array A, there are two islands. (An island is a 4-directio
#nally connected group of 1s not connected to any other 1s.) 
#
# Now, we may change 0s to 1s so as to connect the two islands together to form 
#1 island. 
#
# Return the smallest number of 0s that must be flipped. (It is guaranteed that 
#the answer is at least 1.) 
#
# 
#
# Example 1: 
#
# 
#Input: [[0,1],[1,0]]
#Output: 1
# 
#
# 
# Example 2: 
#
# 
#Input: [[0,1,0],[0,0,0],[0,0,1]]
#Output: 2
# 
#
# 
# Example 3: 
#
# 
#Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
#Output: 1 
#
# 
# 
# 
#
# Note: 
#
# 
# 1 <= A.length = A[0].length <= 100 
# A[i][j] == 0 or A[i][j] == 1 
# 
#
# 
# 
# 
# 
# Related Topics Depth-first Search Breadth-first Search




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        queue = collections.deque()
        visited = set()
        found = False
        for i in range(m):
            if found: break
            for j in range(n):
                if found: break
                if A[i][j] == 1:
                    found = True
                    self.dfs(A, i, j, visited, queue)

        steps = 0
        dirs = [-1, 0, 1, 0, -1]
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for k in range(4):
                    ti = i + dirs[k]
                    tj = j + dirs[k + 1]
                    if ti<0 or ti>=m or tj<0 or tj>=n: continue
                    if (ti, tj) in visited: continue
                    if A[ti][tj] == 1: return steps
                    queue.append((ti, tj))
                    visited.add((ti, tj))
            steps += 1
        return steps

    def dfs(self, A, i, j, visited, queue):
        m, n = len(A), len(A[0])
        if i<0 or i>=m or j<0 or j>=n: return
        if A[i][j] == 0 or (i, j) in visited: return
        queue.append((i, j))
        visited.add((i, j))
        dirs = [-1, 0, 1, 0, -1]
        for k in range(4):
            ti = i+dirs[k]
            tj = j+dirs[k+1]
            self.dfs(A, ti, tj, visited, queue)
        
#leetcode submit region end(Prohibit modification and deletion)
