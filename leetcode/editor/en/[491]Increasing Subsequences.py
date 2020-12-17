# Given an integer array, your task is to find all the different possible increa
# sing subsequences of the given array, and the length of an increasing subsequenc
# e should be at least 2. 
# 
#  
# 
#  Example: 
# 
#  
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4
# ,7,7]]
#  
# 
#  
# 
#  Note: 
# 
#  
#  The length of the given array will not exceed 15. 
#  The range of integer in the given array is [-100,100]. 
#  The given array may contain duplicates, and two equal integers should also be
#  considered as a special case of increasing sequence. 
#  
#  Related Topics Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0: return []
        ans = []

        def dfs(start, n, out, ans):

            if len(out) >= 2:
                ans.append(out[:])
            if start == n: return

            for i in range(start, n):
                if len(out) == 0 or nums[i] >= out[-1]:
                    out.append(nums[i])
                    dfs(i + 1, n, out, ans)
                    out.pop()

        dfs(0, n, [], ans)
        s = set()
        for out in ans: s.add(tuple(out))
        ans = []
        for out in s: ans.append(list(out))
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
