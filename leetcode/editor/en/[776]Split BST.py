# Given a Binary Search Tree (BST) with root node root, and a target value V, sp
# lit the tree into two subtrees where one subtree has nodes that are all smaller 
# or equal to the target value, while the other subtree has all nodes that are gre
# ater than the target value. It's not necessarily the case that the tree contains
#  a node with value V. 
# 
#  Additionally, most of the structure of the original tree should remain. Forma
# lly, for any child C with parent P in the original tree, if they are both in the
#  same subtree after the split, then node C should still have the parent P. 
# 
#  You should output the root TreeNode of both subtrees after splitting, in any 
# order. 
# 
#  Example 1: 
# 
#  
# Input: root = [4,2,6,1,3,5,7], V = 2
# Output: [[2,1],[4,3,6,null,null,5,7]]
# Explanation:
# Note that root, output[0], and output[1] are TreeNode objects, not arrays.
# 
# The given tree [4,2,6,1,3,5,7] is represented by the following diagram:
# 
#           4
#         /   \
#       2      6
#      / \    / \
#     1   3  5   7
# 
# while the diagrams for the outputs are:
# 
#           4
#         /   \
#       3      6      and    2
#             / \           /
#            5   7         1
#  
# 
#  Note: 
# 
#  
#  The size of the BST will not exceed 50. 
#  The BST is always valid and each node's value is different. 
#  Related Topics Tree Recursion


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root: return [None, None]
        if root.val <= V:
            res = self.splitBST(root.right, V)
            root.right = res[0]
            return [root, res[1]]
        else:
            res = self.splitBST(root.left, V)
            root.left = res[1]
            return [res[0], root]
        
# leetcode submit region end(Prohibit modification and deletion)
