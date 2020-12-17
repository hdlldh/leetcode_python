# Remember the story of Little Match Girl? By now, you know exactly what matchst
# icks the little match girl has, please find out a way you can make one square by
#  using up all those matchsticks. You should not break any stick, but you can lin
# k them up, and each matchstick must be used exactly one time. 
# 
#  Your input will be several matchsticks the girl has, represented with their s
# tick length. Your output will either be true or false, to represent whether you 
# could make one square using all the matchsticks the little match girl has. 
# 
#  Example 1: 
#  
# Input: [1,1,2,2,2]
# Output: true
# 
# Explanation: You can form a square with length 2, one side of the square came 
# two sticks with length 1.
#  
#  
# 
#  Example 2: 
#  
# Input: [3,3,3,3,4]
# Output: false
# 
# Explanation: You cannot find a way to form a square with all the matchsticks.
#  
#  
# 
#  Note: 
#  
#  The length sum of the given matchsticks is in the range of 0 to 10^9.
#  The length of the given matchstick array will not exceed 15. 
#  
#  Related Topics Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s%4!=0: return False
        target = s//4
        nums.sort()
        n = len(nums)
        if n<4: return False
        if nums[-1] > target: return False
        visited = [False]*n
        return self.dfs(nums, visited, 4, target, 0, 0)

    def dfs(self, nums, visited, sides, target, curSum,  pos):
        if sides == 1: return True
        if curSum > target: return False
        if curSum == target: return self.dfs(nums, visited, sides-1, target, 0, 0)
        for i in range(pos, len(nums)):
            if visited[i]: continue
            visited[i] = True
            if self.dfs(nums, visited, sides, target, curSum+nums[i], i+1): return True
            visited[i] = False
        return False


# leetcode submit region end(Prohibit modification and deletion)
