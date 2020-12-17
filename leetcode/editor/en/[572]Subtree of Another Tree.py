# Given two non-empty binary trees s and t, check whether tree t has exactly the
#  same structure and node values with a subtree of s. A subtree of s is a tree co
# nsists of a node in s and all of this node's descendants. The tree s could also 
# be considered as a subtree of itself. 
# 
#  Example 1: 
# Given tree s: 
# 
#  
#      3
#     / \
#    4   5
#   / \
#  1   2
#  
# Given tree t:
# 
#  
#    4 
#   / \
#  1   2
#  
# Return true, because t has the same structure and node values with a subtree o
# f s.
# 
#  
# 
#  Example 2: 
# Given tree s: 
# 
#  
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#  
# Given tree t:
# 
#  
#    4
#   / \
#  1   2
#  
# Return false.
# 
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
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s: return t is None
        check = self.helper(s, t)
        if check: return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def helper(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        if s.val != t.val: return False
        return self.helper(s.left, t.left) and self.helper(s.right, t.right)
        
# leetcode submit region end(Prohibit modification and deletion)
