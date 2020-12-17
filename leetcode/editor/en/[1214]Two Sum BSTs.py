# Given two binary search trees, return True if and only if there is a node in t
# he first tree and a node in the second tree whose values sum up to a given integ
# er target. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
# Output: true
# Explanation: 2 and 3 sum up to 5.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  Each tree has at most 5000 nodes. 
#  -10^9 <= target, node.val <= 10^9 
#  
#  Related Topics Binary Search Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        mem = set()

        def inorder(root, mem):
            if not root: return
            mem.add(target - root.val)
            inorder(root.left, mem)
            inorder(root.right, mem)

        def inorder2(root):
            if not root: return False
            if root.val in mem: return True
            left = inorder2(root.left)
            if left: return True
            right = inorder2(root.right)
            if right: return True
            return False

        inorder(root1, mem)
        return inorder2(root2)
        
# leetcode submit region end(Prohibit modification and deletion)
