#Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between). 
#
# 
#For example: 
#Given binary tree [3,9,20,null,null,15,7], 
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7
# 
# 
# 
#return its zigzag level order traversal as: 
# 
#[
#  [3],
#  [20,9],
#  [15,7]
#]
# 
# Related Topics Stack Tree Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
#leetcode submit region end(Prohibit modification and deletion)
