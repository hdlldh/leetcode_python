# Given a binary tree, find the length of the longest path where each node in th
# e path has the same value. This path may or may not pass through the root. 
# 
#  The length of path between two nodes is represented by the number of edges be
# tween them. 
# 
#  
# 
#  Example 1: 
# 
#  Input: 
# 
#  
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
#  
# 
#  Output: 2 
# 
#  
# 
#  Example 2: 
# 
#  Input: 
# 
#  
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
#  
# 
#  Output: 2 
# 
#  
# 
#  Note: The given binary tree has not more than 10000 nodes. The height of the 
# tree is not more than 1000. 
#  Related Topics Tree Recursion


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root: return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if root.left and root.left.val == root.val:
            left = left +1
        else:
            left = 0
        if root.right and root.right.val == root.val:
            right = right + 1
        else:
            right = 0
        self.res = max(self.res, left + right)
        return max(left, right)
# leetcode submit region end(Prohibit modification and deletion)
