#Given a root node reference of a BST and a key, delete the node with the given 
#key in the BST. Return the root node reference (possibly updated) of the BST. 
#
# Basically, the deletion can be divided into two stages:
# 
# Search for a node to remove. 
# If the node is found, delete the node. 
# 
# 
#
# Note: Time complexity should be O(height of tree). 
#
# Example:
# 
#root = [5,3,6,2,4,null,7]
#key = 3
#
#    5
#   / \
#  3   6
# / \   \
#2   4   7
#
#Given key to delete is 3. So we find the node with value 3 and delete it.
#
#One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#
#    5
#   / \
#  4   6
# /     \
#2       7
#
#Another valid answer is [5,2,6,null,4,null,7].
#
#    5
#   / \
#  2   6
#   \   \
#    4   7
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
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return root
        if key >root.val:
            root.right = self.deleteNode(root.right, key)
        elif key<root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left: return root.right
            elif not root.right: return root.left
            else:
                parent = root
                child = root.right
                while child.left is not None:
                    parent = child
                    child = child.left
                if parent != root:
                    parent.left = child.right
                    child.right = root.right
                child.left = root.left
                return child
        return root
        
#leetcode submit region end(Prohibit modification and deletion)
