#Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number. 
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123. 
#
# Find the total sum of all root-to-leaf numbers. 
#
# Note: A leaf is a node with no children. 
#
# Example: 
#
# 
#Input: [1,2,3]
#    1
#   / \
#  2   3
#Output: 25
#Explanation:
#The root-to-leaf path 1->2 represents the number 12.
#The root-to-leaf path 1->3 represents the number 13.
#Therefore, sum = 12 + 13 = 25. 
#
# Example 2: 
#
# 
#Input: [4,9,0,5,1]
#    4
#   / \
#  9   0
# / \
#5   1
#Output: 1026
#Explanation:
#The root-to-leaf path 4->9->5 represents the number 495.
#The root-to-leaf path 4->9->1 represents the number 491.
#The root-to-leaf path 4->0 represents the number 40.
#Therefore, sum = 495 + 491 + 40 = 1026. 
# Related Topics Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.helper(root, 0)
        return self.ans

    def helper(self, root, val):
        if not root: return
        val = 10*val+root.val
        if not root.left and not root.right:
            self.ans+= val
        self.helper(root.left, val)
        self.helper(root.right, val)
        
#leetcode submit region end(Prohibit modification and deletion)
