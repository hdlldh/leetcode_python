#Given the root node of a binary search tree (BST) and a value to be inserted in
#to the tree, insert the value into the BST. Return the root node of the BST afte
#r the insertion. It is guaranteed that the new value does not exist in the origi
#nal BST. 
#
# Note that there may exist multiple valid ways for the insertion, as long as th
#e tree remains a BST after insertion. You can return any of them. 
#
# For example, 
#
# 
#Given the tree:
#        4
#       / \
#      2   7
#     / \
#    1   3
#And the value to insert: 5
# 
#
# You can return this binary search tree: 
#
# 
#         4
#       /   \
#      2     7
#     / \   /
#    1   3 5
# 
#
# This tree is also valid: 
#
# 
#         5
#       /   \
#      2     7
#     / \   
#    1   3
#         \
#          4
# 
# Related Topics Tree




#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            node = TreeNode(val)
            return node
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
#leetcode submit region end(Prohibit modification and deletion)
