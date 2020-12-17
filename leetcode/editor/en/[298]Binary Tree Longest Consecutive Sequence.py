#Given a binary tree, find the length of the longest consecutive sequence path. 
#
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse). 
#
# Example 1: 
#
# 
#Input:
#
#   1
#    \
#     3
#    / \
#   2   4
#        \
#         5
#
#Output: 3
#
#Explanation: Longest consecutive sequence path is 3-4-5, so return 3. 
#
# Example 2: 
#
# 
#Input:
#
#   2
#    \
#     3
#    / 
#   2    
#  / 
# 1
#
#Output: 2 
#
#Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2. Related Topics Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root: return 0
        length = 1
        left = self.helper(root.left)
        right = self.helper(root.right)
        if root.left and root.left.val == root.val+1:
            length = max(length, left+1)
        if root.right and root.right.val == root.val+1:
            length = max(length, right+1)
        self.ans = max(self.ans, length)
        return length




        
#leetcode submit region end(Prohibit modification and deletion)
