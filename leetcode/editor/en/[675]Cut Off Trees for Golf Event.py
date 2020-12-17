#You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map: 
#
# 
# 0 represents the obstacle can't be reached. 
# 1 represents the ground can be walked through. 
# The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height. 
# 
#
# 
#
# You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1). 
#
# You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation. 
#
# You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off. 
#
# Example 1: 
#
# 
#Input: 
#[
# [1,2,3],
# [0,0,4],
# [7,6,5]
#]
#Output: 6
# 
#
# 
#
# Example 2: 
#
# 
#Input: 
#[
# [1,2,3],
# [0,0,0],
# [7,6,5]
#]
#Output: -1
# 
#
# 
#
# Example 3: 
#
# 
#Input: 
#[
# [2,3,4],
# [0,0,5],
# [8,7,6]
#]
#Output: 6
#Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
# 
#
# 
#
# Hint: size of the given matrix will not exceed 50x50. 
# Related Topics Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        m, n = len(forest), len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] >1: trees.append([forest[i][j], i, j])
        trees.sort()
        si = 0
        sj = 0
        ans = 0
        for i in range(len(trees)):
            ei = trees[i][1]
            ej = trees[i][2]
            cnt = self.bfs(forest, si, sj, ei, ej)
            if cnt == -1: return -1
            ans += cnt
            si = ei
            sj = ej
        return ans


    def bfs(self, forest, si, sj, ei, ej):
        if si==ei and sj == ej: return 0
        m, n = len(forest), len(forest[0])
        queue = collections.deque()
        queue.append((si, sj))
        visited = set()
        visited.add((si, sj))
        ans = 0
        di = [0, -1, 0, 1]
        dj = [-1, 0, 1, 0]
        while queue:
            ans += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for k in range(4):
                    ni = i+di[k]
                    nj = j+dj[k]
                    if ni<0 or ni>=m or nj<0 or nj>=n: continue
                    if ni == ei and nj == ej: return ans
                    if (ni, nj) in visited: continue
                    if forest[ni][nj] == 0: continue
                    queue.append((ni, nj))
                    visited.add((ni, nj))
        return -1




#leetcode submit region end(Prohibit modification and deletion)
