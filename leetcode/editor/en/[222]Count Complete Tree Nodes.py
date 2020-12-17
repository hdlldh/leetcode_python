#Given a complete binary tree, count the number of nodes. 
#
# Note: 
#
# Definition of a complete binary tree from Wikipedia: 
#In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h. 
#
# Example: 
#
# 
#Input: 
#    1
#   / \
#  2   3
# / \  /
#4  5 6
#
#Output: 6 
# Related Topics Binary Search Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l=root
        lh = 0
        while l:
            lh+=1
            l = l.left
        r=root;
        rh=0
        while r:
            rh+=1
            r = r.right
        if lh==rh: return 2**lh-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        
#leetcode submit region end(Prohibit modification and deletion)
