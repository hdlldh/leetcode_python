#Given a binary tree, return all root-to-leaf paths. 
#
# Note: A leaf is a node with no children. 
#
# Example: 
#
# 
#Input:
#
#   1
# /   \
#2     3
# \
#  5
#
#Output: ["1->2->5", "1->3"]
#
#Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# Related Topics Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        self.helper(root, [], ans)
        return ans

    def helper(self, root, path, ans):
        if not root: return
        if not root.left and not root.right:
            path.append(root.val)
            ans.append('->'.join([str(p) for p in path]))
            path.pop()
        self.helper(root.left, path+[root.val],ans)
        self.helper(root.right, path + [root.val], ans)
#leetcode submit region end(Prohibit modification and deletion)
