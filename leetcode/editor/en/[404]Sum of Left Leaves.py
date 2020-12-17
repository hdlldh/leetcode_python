#Find the sum of all left leaves in a given binary tree. 
#
# Example:
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7
#
#There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
# 
# Related Topics Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.helper(root, False)
        return self.ans

    def helper(self, root, left):
        if not root: return
        if not root.left and not root.right and left:
            self.ans += root.val
        self.helper(root.left, True)
        self.helper(root.right, False)

        
#leetcode submit region end(Prohibit modification and deletion)
