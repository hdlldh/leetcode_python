#On a 2D plane, we place stones at some integer coordinate points. Each coordinate point may have at most one stone. 
#
# Now, a move consists of removing a stone that shares a column or row with another stone on the grid. 
#
# What is the largest possible number of moves we can make? 
#
# 
#
# 
# Example 1: 
#
# 
#Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
#Output: 5
# 
#
# 
# Example 2: 
#
# 
#Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
#Output: 3
# 
#
# 
# Example 3: 
#
# 
#Input: stones = [[0,0]]
#Output: 0
# 
#
# 
#
# Note: 
#
# 
# 1 <= stones.length <= 1000 
# 0 <= stones[i][j] < 10000 
# 
# 
# 
# 
# Related Topics Depth-first Search Union Find



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        roots = set()
        parent = [i for i in range(20000)]
        for x, y in stones:
            self.union(parent, x, y+10000)

        for x, y in stones:
            roots.add(self.find(parent, x))
        return n-len(roots)

    def find(self, parent, i):
        while i!= parent[i]: i = parent[i]
        return i

    def union(self, parent, i, j):
        root_i = self.find(parent, i)
        root_j = self.find(parent, j)
        if root_i!=root_j: parent[root_j] = root_i

        
#leetcode submit region end(Prohibit modification and deletion)
