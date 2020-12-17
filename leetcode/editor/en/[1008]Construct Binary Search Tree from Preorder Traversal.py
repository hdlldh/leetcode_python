# Return the root node of a binary search tree that matches the given preorder t
# raversal. 
# 
#  (Recall that a binary search tree is a binary tree where for every node, any 
# descendant of node.left has a value < node.val, and any descendant of node.right
#  has a value > node.val. Also recall that a preorder traversal displays the valu
# e of the node first, then traverses node.left, then traverses node.right.) 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= preorder.length <= 100 
#  The values of preorder are distinct. 
#  
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        inorder = sorted(preorder)

        def build(preorder, inorder):
            if len(inorder) == 0: return None
            val = preorder[0]
            preorder.pop(0)
            idx = inorder.index(val)
            node = TreeNode(val)
            node.left = build(preorder, inorder[:idx])
            node.right = build(preorder, inorder[idx + 1:])
            return node

        return build(preorder, inorder)
        
# leetcode submit region end(Prohibit modification and deletion)
