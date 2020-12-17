#Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum. 
#
# Note: A leaf is a node with no children. 
#
# Example: 
#
# Given the below binary tree and sum = 22, 
#
# 
#      5
#     / \
#    4   8
#   /   / \
#  11  13  4
# /  \    / \
#7    2  5   1
# 
#
# Return: 
#
# 
#[
#   [5,4,11,2],
#   [5,8,4,5]
#]
# 
# Related Topics Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
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
        :rtype: List[List[int]]
        """
        ans = []
        self.helper(root, sum, [], ans)
        return ans

    def helper(self, root, sum, path, ans):
        if not root: return
        if not root.left and not root.right and root.val == sum:
            path.append(root.val)
            ans.append(path)
        self.helper(root.left, sum-root.val, path+[root.val], ans)
        self.helper(root.right, sum-root.val, path+[root.val], ans)
        
#leetcode submit region end(Prohibit modification and deletion)
