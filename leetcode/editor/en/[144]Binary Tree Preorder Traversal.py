#Given a binary tree, return the preorder traversal of its nodes' values. 
#
# Example: 
#
# 
#Input: [1,null,2,3]
#   1
#    \
#     2
#    /
#   3
#
#Output: [1,2,3]
# 
#
# Follow up: Recursive solution is trivial, could you do it iteratively? 
# Related Topics Stack Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if not root: return
        ans.append(root.val)
        self.helper(root.left, ans)
        self.helper(root.right, ans)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root: return ans
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.pop()
            ans.append(node.val)
            if node.right: queue.append(node.right)
            if node.left: queue.append(node.left)
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
