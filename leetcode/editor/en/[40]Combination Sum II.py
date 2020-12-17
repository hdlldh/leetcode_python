#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target. 
#
# Each number in candidates may only be used once in the combination. 
#
# Note: 
#
# 
# All numbers (including target) will be positive integers. 
# The solution set must not contain duplicate combinations. 
# 
#
# Example 1: 
#
# 
#Input: candidates = [10,1,2,7,6,1,5], target = 8,
#A solution set is:
#[
#  [1, 7],
#  [1, 2, 5],
#  [2, 6],
#  [1, 1, 6]
#]
# 
#
# Example 2: 
#
# 
#Input: candidates = [2,5,2,1,2], target = 5,
#A solution set is:
#[
#  [1,2,2],
#  [5]
#]
# 
# Related Topics Array Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        visited = [0] * len(candidates)
        self.dfs(candidates, target, 0, [], ans, visited)
        return ans

    def dfs(self, candidates, target, start, out, ans, visited):
        if target <0: return
        if target==0:
            ans.append(out[:])
            return
        for i in range(start, len(candidates)):
            if visited[i] == 1: continue
            if i==0 or candidates[i]!=candidates[i-1] or visited[i-1]==1:
                visited[i] = 1
                out.append(candidates[i])
                self.dfs(candidates, target-candidates[i], i+1, out, ans, visited)
                visited[i] = 0
                out.pop()


        
#leetcode submit region end(Prohibit modification and deletion)
