#Given inorder and postorder traversal of a tree, construct the binary tree. 
#
# Note: 
#You may assume that duplicates do not exist in the tree. 
#
# For example, given 
#
# 
#inorder = [9,3,15,20,7]
#postorder = [9,15,7,20,3] 
#
# Return the following binary tree: 
#
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7
# 
# Related Topics Array Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        return self.helper(inorder, 0, n-1, postorder, 0, n-1)

    def helper(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if inStart>inEnd or postStart>postEnd: return None
        root = TreeNode(postorder[postEnd])
        k = inorder.index(postorder[postEnd])
        root.left = self.helper(inorder, inStart, k-1, postorder, postStart, postStart+k-inStart-1)
        root.right = self.helper(inorder, k+1, inEnd, postorder, postEnd +k-inEnd, postEnd-1)
        return root
        
#leetcode submit region end(Prohibit modification and deletion)
