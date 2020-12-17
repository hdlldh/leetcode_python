#Given a set of distinct integers, nums, return all possible subsets (the power set). 
#
# Note: The solution set must not contain duplicate subsets. 
#
# Example: 
#
# 
#Input: nums = [1,2,3]
#Output:
#[
#  [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
#] 
# Related Topics Array Backtracking Bit Manipulation



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(nums,0, [], ans)
        return ans

    def dfs(self, nums, start, out, ans):
        if nums and start==len(nums):
            ans.append(out)
            return
        self.dfs(nums, start+1,out+[nums[start]], ans)
        self.dfs(nums, start+1, out, ans)

#leetcode submit region end(Prohibit modification and deletion)
