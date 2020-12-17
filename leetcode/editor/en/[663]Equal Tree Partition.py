# 
# Given a binary tree with n nodes, your task is to check if it's possible to pa
# rtition the tree to two trees which have the equal sum of values after removing 
# exactly one edge on the original tree.
#  
# 
#  Example 1: 
#  
# Input:     
#     5
#    / \
#   10 10
#     /  \
#    2   3
# 
# Output: True
# Explanation: 
#     5
#    / 
#   10
#       
# Sum: 15
# 
#    10
#   /  \
#  2    3
# 
# Sum: 15
#  
#  
# 
# 
#  Example 2: 
#  
# Input:     
#     1
#    / \
#   2  10
#     /  \
#    2   20
# 
# Output: False
# Explanation: You can't split the tree into two trees with equal sum after remo
# ving exactly one edge on the tree.
#  
#  
# 
#  Note: 
#  
#  The range of tree node value is in the range of [-100000, 100000]. 
#  1 <= n <= 10000 
#  
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s = self.helper1(root)
        self.ans = False
        self.helper2(root, root, s)
        return self.ans

    def helper1(self, root):
        if not root: return 0
        return self.helper1(root.left)+self.helper1(root.right) + root.val

    def helper2(self, root, root0, s):
        if not root: return 0
        c = self.helper2(root.left,root0, s) + self.helper2(root.right,root0,s) + root.val
        if c == s-c and root!=root0:
            self.ans = True
        return c
# leetcode submit region end(Prohibit modification and deletion)
