#Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it. 
#
# Note: 
#A subtree must include all of its descendants. 
#
# Example: 
#
# 
#Input: [10,5,15,1,8,null,7]
#
#   10 
#   / \ 
#  5  15 
# / \   \ 
#1   8   7
#
#Output: 3
#Explanation: The Largest BST Subtree in this case is the highlighted one.
#             The return value is the subtree's size, which is 3.
# 
#
# Follow up: 
#Can you figure out ways to solve it with O(n) time complexity? 
# Related Topics Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans, _, _, _, = self.helper(root)
        return ans

    def helper(self, root):
        if not root: return (0, True, float('inf'), -float('inf'))
        lsize, lbst, lmin, lmax = self.helper(root.left)
        rsize, rbst, rmin, rmax = self.helper(root.right)
        if lbst and rbst and root.val>lmax and root.val<rmin:
            lmin = min(lmin, root.val)
            rmax = max(rmax, root.val)
            return (lsize+rsize+1, True, lmin, rmax)
        return (max(lsize, rsize), False, None, None)

#leetcode submit region end(Prohibit modification and deletion)
