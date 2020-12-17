# Given a binary search tree, return a balanced binary search tree with the same
#  node values. 
# 
#  A binary search tree is balanced if and only if the depth of the two subtrees
#  of every node never differ by more than 1. 
# 
#  If there is more than one answer, return any of them. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is 
# also correct.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is between 1 and 10^4. 
#  The tree nodes will have distinct values between 1 and 10^5. 
#  Related Topics Binary Search Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        vals = []

        def inorder(root, vals):
            if not root: return
            inorder(root.left, vals)
            vals.append(root.val)
            inorder(root.right, vals)

        inorder(root, vals)

        def build(vals, l, r):
            if l>r: return None
            mid = l + (r-l)//2
            node = TreeNode(vals[mid])
            node.left = build(vals, l, mid -1)
            node.right = build(vals, mid+1, r)
            return node
        return build(vals, 0, len(vals)-1)

        
# leetcode submit region end(Prohibit modification and deletion)
