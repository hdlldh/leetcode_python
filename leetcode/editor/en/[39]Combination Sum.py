#Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target. 
#
# The same repeated number may be chosen from candidates unlimited number of times. 
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
#Input: candidates = [2,3,6,7], target = 7,
#A solution set is:
#[
#  [7],
#  [2,2,3]
#]
# 
#
# Example 2: 
#
# 
#Input: candidates = [2,3,5], target = 8,
#A solution set is:
#[
#  [2,2,2,2],
#  [2,3,3],
#  [3,5]
#]
# 
# Related Topics Array Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        return ans

    def dfs(self, candidates, target, start, out, ans):
        if target <0: return
        if target == 0:
            ans.append(out[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target: break
            out.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i, out, ans)
            out.pop()


#leetcode submit region end(Prohibit modification and deletion)
