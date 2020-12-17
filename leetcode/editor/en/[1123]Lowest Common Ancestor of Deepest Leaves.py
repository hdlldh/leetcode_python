# Given a rooted binary tree, return the lowest common ancestor of its deepest l
# eaves. 
# 
#  Recall that: 
# 
#  
#  The node of a binary tree is a leaf if and only if it has no children 
#  The depth of the root of the tree is 0, and if the depth of a node is d, the 
# depth of each of its children is d+1. 
#  The lowest common ancestor of a set S of nodes is the node A with the largest
#  depth such that every node in S is in the subtree with root A. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3]
# Output: [1,2,3]
# Explanation: 
# The deepest leaves are the nodes with values 2 and 3.
# The lowest common ancestor of these leaves is the node with value 1.
# The answer returned is a TreeNode object (not an array) with serialization "[1
# ,2,3]".
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,3,4]
# Output: [4]
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1,2,3,4,5]
# Output: [2,4,5]
#  
# 
#  
#  Constraints: 
# 
#  
#  The given tree will have between 1 and 1000 nodes. 
#  Each node of the tree will have a distinct value between 1 and 1000. 
#  
#  Related Topics Tree Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        mem = {}
        return self.helper(root, mem)

    def helper(self, root, mem):
        if not root: return root
        left = self.get_depth(root.left, mem)
        right = self.get_depth(root.right, mem)
        if left == right: return root
        if left > right:
            return self.helper(root.left, mem)
        else:
            return self.helper(root.right, mem)

    def get_depth(self, root, mem):
        if not root: return 0
        if root in mem: return mem[root]
        mem[root] = max(self.get_depth(root.left, mem), self.get_depth(root.right, mem)) + 1
        return mem[root]
        
# leetcode submit region end(Prohibit modification and deletion)
