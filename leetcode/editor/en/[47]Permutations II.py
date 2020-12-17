#Given a collection of numbers that might contain duplicates, return all possible unique permutations. 
#
# Example: 
#
# 
#Input: [1,1,2]
#Output:
#[
#  [1,1,2],
#  [1,2,1],
#  [2,1,1]
#]
# 
# Related Topics Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        visited = [0] * len(nums)
        self.dfs(nums, [], ans, visited)
        return ans

    def dfs(self, nums, sol, ans, visited):
        if len(sol) == len(nums):
            ans.append(sol)
            return
        for i, num in enumerate(nums):
            if visited[i]==1:continue
            if i==0 or nums[i]!=nums[i-1] or visited[i-1]==1:
                visited[i] = 1
                self.dfs(nums, sol+[num], ans, visited)
                visited[i] = 0

#leetcode submit region end(Prohibit modification and deletion)
