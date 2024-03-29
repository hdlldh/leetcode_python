#Given a binary tree, determine if it is a valid binary search tree (BST). 
#
# Assume a BST is defined as follows: 
#
# 
# The left subtree of a node contains only nodes with keys less than the node's key. 
# The right subtree of a node contains only nodes with keys greater than the node's key. 
# Both the left and right subtrees must also be binary search trees. 
# 
#
# 
#
# Example 1: 
#
# 
#    2
#   / \
#  1   3
#
#Input: [2,1,3]
#Output: true
# 
#
# Example 2: 
#
# 
#    5
#   / \
#  1   4
#     / \
#    3   6
#
#Input: [5,1,4,null,null,3,6]
#Output: false
#Explanation: The root node's value is 5 but its right child's value is 4.
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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, root, lower, upper):
        if not root: return True
        if root.val >=upper or root.val <=lower: return False

        left = self.helper(root.left, lower, root.val)
        right = self.helper(root.right, root.val, upper)
        return left and right
        
#leetcode submit region end(Prohibit modification and deletion)
