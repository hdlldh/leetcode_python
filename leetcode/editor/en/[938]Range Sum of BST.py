# Given the root node of a binary search tree, return the sum of values of all n
# odes with value between L and R (inclusive). 
# 
#  The binary search tree is guaranteed to have unique values. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
#  
# 
#  
#  Example 2: 
# 
#  
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
#  
# 
#  
# 
#  Note: 
# 
#  
#  The number of nodes in the tree is at most 10000. 
#  The final answer is guaranteed to be less than 2^31. 
#  
#  
#  Related Topics Tree Recursion


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.ans = 0
        self.inorder(root, L, R)
        return self.ans

    def inorder(self, root, L, R):
        if not root: return
        self.inorder(root.left, L, R)
        if root.val >= L and root.val <= R:
            self.ans += root.val
        if root.val > R: return
        self.inorder(root.right, L, R)

        
# leetcode submit region end(Prohibit modification and deletion)
