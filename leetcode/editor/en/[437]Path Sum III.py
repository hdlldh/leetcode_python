# You are given a binary tree in which each node contains an integer value. 
# 
#  Find the number of paths that sum to a given value. 
# 
#  The path does not need to start or end at the root or a leaf, but it must go 
# downwards
# (traveling only from parent nodes to child nodes). 
# 
#  The tree has no more than 1,000 nodes and the values are in the range -1,000,
# 000 to 1,000,000.
# 
#  Example:
#  
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.numOfPaths = 0
        self.dfs(root, sum)
        return self.numOfPaths

    def dfs(self, node, target):
        if not node: return
        self.count(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def count(self, node, target):
        if not node: return
        if node.val == target:
            self.numOfPaths += 1
        self.count(node.left, target - node.val)
        self.count(node.right, target - node.val)
        
# leetcode submit region end(Prohibit modification and deletion)
