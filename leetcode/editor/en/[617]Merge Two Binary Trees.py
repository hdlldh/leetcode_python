# Given two binary trees and imagine that when you put one of them to cover the 
# other, some nodes of the two trees are overlapped while the others are not. 
# 
#  You need to merge them into a new binary tree. The merge rule is that if two 
# nodes overlap, then sum node values up as the new value of the merged node. Othe
# rwise, the NOT null node will be used as the node of new tree. 
# 
#  Example 1: 
# 
#  
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
#  
# 
#  
# 
#  Note: The merging process must start from the root nodes of both trees. 
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1: return t2
        if not t2: return t1
        node = TreeNode(t1.val+t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node
# leetcode submit region end(Prohibit modification and deletion)
