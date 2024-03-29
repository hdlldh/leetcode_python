#Given a binary tree rooted at root, the depth of each node is the shortest dist
#ance to the root. 
#
# A node is deepest if it has the largest depth possible among any node in the e
#ntire tree. 
#
# The subtree of a node is that node, plus the set of all descendants of that no
#de. 
#
# Return the node with the largest depth such that it contains all the deepest n
#odes in its subtree. 
#
# 
#
# Example 1: 
#
# 
#Input: [3,5,1,6,2,0,8,null,null,7,4]
#Output: [2,7,4]
#Explanation:
#
#
#
#We return the node with value 2, colored in yellow in the diagram.
#The nodes colored in blue are the deepest nodes of the tree.
#The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the g
#iven tree.
#The output "[2, 7, 4]" is a serialization of the subtree rooted at the node wit
#h value 2.
#Both the input and output have TreeNode type.
# 
#
# 
#
# Note: 
#
# 
# The number of nodes in the tree will be between 1 and 500. 
# The values of each node are unique. 
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
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        _, ans = self.helper(root)
        return ans

    def helper(self, root):
        if not root: return 0, None
        ld, ltree = self.helper(root.left)
        rd, rtree = self.helper(root.right)
        if ld==rd: return ld+1, root
        if ld> rd:
            return ld+1, ltree
        else:
            return rd+1, rtree
        
#leetcode submit region end(Prohibit modification and deletion)
