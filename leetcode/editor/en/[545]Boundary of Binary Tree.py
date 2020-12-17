# Given a binary tree, return the values of its boundary in anti-clockwise direc
# tion starting from root. Boundary includes left boundary, leaves, and right boun
# dary in order without duplicate nodes. (The values of the nodes may still be dup
# licates.) 
# 
#  Left boundary is defined as the path from root to the left-most node. Right b
# oundary is defined as the path from root to the right-most node. If the root doe
# sn't have left subtree or right subtree, then the root itself is left boundary o
# r right boundary. Note this definition only applies to the input binary tree, an
# d not applies to any subtrees. 
# 
#  The left-most node is defined as a leaf node you could reach when you always 
# firstly travel to the left subtree if exists. If not, travel to the right subtre
# e. Repeat until you reach a leaf node. 
# 
#  The right-most node is also defined by the same way with left and right excha
# nged. 
# 
#  Example 1 
# 
#  
# Input:
#   1
#    \
#     2
#    / \
#   3   4
# 
# Ouput:
# [1, 3, 4, 2]
# 
# Explanation:
# The root doesn't have left subtree, so the root itself is left boundary.
# The leaves are node 3 and 4.
# The right boundary are node 1,2,4. Note the anti-clockwise direction means you
#  should output reversed right boundary.
# So order them in anti-clockwise without duplicates and we have [1,3,4,2].
#  
# 
#  
# 
#  Example 2 
# 
#  
# Input:
#     ____1_____
#    /          \
#   2            3
#  / \          / 
# 4   5        6   
#    / \      / \
#   7   8    9  10  
#        
# Ouput:
# [1,2,4,7,8,9,10,6,3]
# 
# Explanation:
# The left boundary are node 1,2,4. (4 is the left-most node according to defini
# tion)
# The leaves are node 4,7,8,9,10.
# The right boundary are node 1,3,6,10. (10 is the right-most node).
# So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,1
# 0,6,3].
#  
# 
#  
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root: return ans
        ans.append(root.val)
        if self.isLeaf(root): return ans
        self.leftBoundary(root.left, ans)
        self.leaves(root, ans)
        self.rightBoundary(root.right, ans)
        return ans

    def isLeaf(self, root):
        return not root.left and not root.right

    def leftBoundary(self, root, ans):
        if not root or self.isLeaf(root): return
        ans.append(root.val)
        if not root.left: self.leftBoundary(root.right, ans)
        else: self.leftBoundary(root.left, ans)

    def rightBoundary(self, root, ans):
        if not root or self.isLeaf(root): return
        if not root.right: self.rightBoundary(root.left, ans)
        else: self.rightBoundary(root.right, ans)
        ans.append(root.val)

    def leaves(self, root, ans):
        if not root: return
        if self.isLeaf(root): ans.append(root.val)
        self.leaves(root.left, ans)
        self.leaves(root.right, ans)
        
# leetcode submit region end(Prohibit modification and deletion)
