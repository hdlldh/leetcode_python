# Given the root of a binary tree, then value v and depth d, you need to add a r
# ow of nodes with value v at the given depth d. The root node is at depth 1. 
# 
#  The adding rule is: given a positive integer depth d, for each NOT null tree 
# nodes N in depth d-1, create two tree nodes with value v as N's left subtree roo
# t and right subtree root. And N's original left subtree should be the left subtr
# ee of the new left subtree root, its original right subtree should be the right 
# subtree of the new right subtree root. If depth d is 1 that means there is no de
# pth d-1 at all, then create a tree node with value v as the new root of the whol
# e original tree, and the original tree is the new root's left subtree. 
# 
#  Example 1: 
#  
# Input: 
# A binary tree as following:
#        4
#      /   \
#     2     6
#    / \   / 
#   3   1 5   
# 
# v = 1
# 
# d = 2
# 
# Output: 
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     / 
#  3   1   5   
# 
#  
#  
# 
# 
#  Example 2: 
#  
# Input: 
# A binary tree as following:
#       4
#      /   
#     2    
#    / \   
#   3   1    
# 
# v = 1
# 
# d = 3
# 
# Output: 
#       4
#      /   
#     2
#    / \    
#   1   1
#  /     \  
# 3       1
#  
#  
# 
#  Note: 
#  
#  The given d is in range [1, maximum depth of the given tree + 1]. 
#  The given binary tree has at least one tree node. 
#  
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root: return None
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        queue = collections.deque()
        queue.append([root, 1])

        while queue:
            cur, cur_d = queue.popleft()
            if cur_d < d-1:
                if cur.left: queue.append([cur.left, cur_d + 1])
                if cur.right: queue.append([cur.right, cur_d + 1])
            elif cur_d == d -1:
                t = TreeNode(v)
                t.left = cur.left
                cur.left = t
                t = TreeNode(v)
                t.right = cur.right
                cur.right = t
            else: break
        return root
        
# leetcode submit region end(Prohibit modification and deletion)
