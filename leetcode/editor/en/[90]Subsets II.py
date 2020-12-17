#Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set). 
#
# Note: The solution set must not contain duplicate subsets. 
#
# Example: 
#
# 
#Input: [1,2,2]
#Output:
#[
#  [2],
#  [1],
#  [1,2,2],
#  [2,2],
#  [1,2],
#  []
#]
# 
# Related Topics Array Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        visited = [0] *len(nums)
        ans = []
        self.dfs(nums, 0, visited, [], ans)
        return ans

    def dfs(self, nums, start, visited, out, ans):
        if start==len(nums):
            ans.append(out[:])
            return
        self.dfs(nums, start + 1, visited, out, ans)
        if start==0 or nums[start]!=nums[start-1] or visited[start-1]==1:
            out.append(nums[start])
            visited[start] = 1
            self.dfs(nums, start+1, visited, out, ans)
            out.pop()
            visited[start] = 0

#leetcode submit region end(Prohibit modification and deletion)
