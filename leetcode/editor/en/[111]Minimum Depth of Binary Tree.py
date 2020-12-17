#Given a binary tree, find its minimum depth. 
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node. 
#
# Note: A leaf is a node with no children. 
#
# Example: 
#
# Given binary tree [3,9,20,null,null,15,7], 
#
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7 
#
# return its minimum depth = 2. 
# Related Topics Tree Depth-first Search Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not root.left and not root.right: return 1
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
        elif root.left:
            return self.minDepth(root.left) + 1
        else:
            return self.minDepth(root.right)+1
        
#leetcode submit region end(Prohibit modification and deletion)
