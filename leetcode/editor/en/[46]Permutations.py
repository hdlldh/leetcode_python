#Given a collection of distinct integers, return all possible permutations. 
#
# Example: 
#
# 
#Input: [1,2,3]
#Output:
#[
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
#]
# 
# Related Topics Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        visited = [0] * len(nums)
        self.dfs(nums, [], ans, visited)
        return ans

    def dfs(self, nums, sol, ans, visited):
        if len(sol) == len(nums):
            ans.append(sol)
            return
        for i, num in enumerate(nums):
            if visited[i]==1:continue
            visited[i] = 1
            self.dfs(nums, sol+[num], ans, visited)
            visited[i] = 0
#leetcode submit region end(Prohibit modification and deletion)
