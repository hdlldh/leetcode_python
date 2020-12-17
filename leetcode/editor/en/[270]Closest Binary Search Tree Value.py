#Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target. 
#
# Note: 
#
# 
# Given target value is a floating point. 
# You are guaranteed to have only one unique value in the BST that is closest to the target. 
# 
#
# Example: 
#
# 
#Input: root = [4,2,5,1,3], target = 3.714286
#
#    4
#   / \
#  2   5
# / \
#1   3
#
#Output: 4
# 
# Related Topics Binary Search Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.minGap = float('inf')
        self.ans = None
        self.helper(root, target)
        return self.ans

    def helper(self, root, target):
        if not root: return None
        if root.val>= target:
            self.helper(root.left, target)
        gap = abs(root.val-target)
        if gap<self.minGap:
            self.minGap = gap
            self.ans = root.val
        if root.val<=target:
            self.helper(root.right, target)



        
#leetcode submit region end(Prohibit modification and deletion)
