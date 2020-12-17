#Given a non-empty binary tree, find the maximum path sum. 
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root. 
#
# Example 1: 
#
# 
#Input: [1,2,3]
#
#       1
#      / \
#     2   3
#
#Output: 6
# 
#
# Example 2: 
#
# 
#Input: [-10,9,20,null,null,15,7]
#
#   -10
#   / \
#  9  20
#    /  \
#   15   7
#
#Output: 42
# 
# Related Topics Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = -float('inf')
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root: return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.ans = max(self.ans, root.val, root.val+left, root.val+right,root.val+left+right )
        return max(left+root.val, right+root.val, root.val)
        
#leetcode submit region end(Prohibit modification and deletion)
