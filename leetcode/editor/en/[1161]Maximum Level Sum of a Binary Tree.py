# Given the root of a binary tree, the level of its root is 1, the level of its 
# children is 2, and so on. 
# 
#  Return the smallest level X such that the sum of all the values of nodes at l
# evel X is maximal. 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The number of nodes in the given tree is between 1 and 10^4. 
#  -10^5 <= node.val <= 10^5 
#  
#  Related Topics Graph


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = collections.deque()
        queue.append(root)
        level = 0
        ans = 0
        mxi = -float('inf')
        while queue:
            size = len(queue)
            level += 1
            s = 0
            for _ in range(size):
                node = queue.popleft()
                s += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if s > mxi:
                mxi = s
                ans = level
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
