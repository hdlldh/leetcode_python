#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center). 
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric: 
#
# 
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
# 
#
# 
#
# But the following [1,2,2,null,3,null,3] is not: 
#
# 
#    1
#   / \
#  2   2
#   \   \
#   3    3
# 
#
# 
#
# Note: 
#Bonus points if you could solve it both recursively and iteratively. 
# Related Topics Tree Depth-first Search Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)

    def isMirror(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        return root1.val==root2.val and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
        
#leetcode submit region end(Prohibit modification and deletion)
