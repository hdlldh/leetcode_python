# 
# Given a binary tree, you need to compute the length of the diameter of the tre
# e. The diameter of a binary tree is the length of the longest path between any t
# wo nodes in a tree. This path may or may not pass through the root.
#  
# 
#  
# Example: 
# Given a binary tree 
#  
#           1
#          / \
#         2   3
#        / \     
#       4   5    
#  
#  
#  
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#  
# 
#  Note:
# The length of path between two nodes is represented by the number of edges bet
# ween them.
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root: return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.ans = max(self.ans, left + right)
        return max(left, right) + 1
        
# leetcode submit region end(Prohibit modification and deletion)
