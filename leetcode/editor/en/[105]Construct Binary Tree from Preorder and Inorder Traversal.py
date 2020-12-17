#Given preorder and inorder traversal of a tree, construct the binary tree. 
#
# Note: 
#You may assume that duplicates do not exist in the tree. 
#
# For example, given 
#
# 
#preorder = [3,9,20,15,7]
#inorder = [9,3,15,20,7] 
#
# Return the following binary tree: 
#
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7 
# Related Topics Array Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        return self.helper(preorder, 0, n - 1, inorder, 0, n - 1)

    def helper(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd: return None
        root = TreeNode(preorder[preStart])
        k = inorder.index(preorder[preStart])
        root.left = self.helper(preorder, preStart+1, preStart+k-inStart, inorder, inStart, k - 1)
        root.right = self.helper(preorder, preEnd-inEnd+k+1, preEnd, inorder, k+1, inEnd)
        return root
        
#leetcode submit region end(Prohibit modification and deletion)
