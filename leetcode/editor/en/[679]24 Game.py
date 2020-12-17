# 
# You have 4 cards each containing a number from 1 to 9. You need to judge wheth
# er they could operated through *, /, +, -, (, ) to get the value of 24.
#  
# 
#  Example 1: 
#  
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
#  
#  
# 
#  Example 2: 
#  
# Input: [1, 2, 1, 2]
# Output: False
#  
#  
# 
#  Note: 
#  
#  The division operator / represents real division, not integer division. For e
# xample, 4 / (1 - 2/3) = 12. 
#  Every operation done is between two numbers. In particular, we cannot use - a
# s a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 -
#  1 - 1 - 1 is not allowed. 
#  You cannot concatenate numbers together. For example, if the input is [1, 2, 
# 1, 2], we cannot write this as 12 + 12. 
#  
#  
#  Related Topics Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        eps = 1e-6
        ops = ['+','-','*','/']
        return self.dfs(nums, eps, ops)

    def dfs(self, nums, eps, ops):
        if len(nums) == 1:
            if abs(nums[0]-24)<eps: return True
            else: return False
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i==j: continue
                t = []
                for k in range(n):
                    if k!=i and k!=j: t.append(nums[k])
                for op in ops:
                    if op in ['+','*'] and i>j: continue
                    if op=='/' and abs(nums[j])< eps: continue
                    if op == '+': t.append(nums[i]+nums[j])
                    elif op=='-': t.append(nums[i] - nums[j])
                    elif op == '*': t.append(nums[i] * nums[j])
                    else: t.append(nums[i] / float(nums[j]))
                    if self.dfs(t, eps, ops): return True
                    t.pop()
        return False




        
# leetcode submit region end(Prohibit modification and deletion)
