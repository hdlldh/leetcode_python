#Given a binary tree, return the inorder traversal of its nodes' values. 
#
# Example: 
#
# 
#Input: [1,null,2,3]
#   1
#    \
#     2
#    /
#   3
#
#Output: [1,3,2] 
#
# Follow up: Recursive solution is trivial, could you do it iteratively? 
# Related Topics Hash Table Stack Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if not root: return
        self.helper(root.left, ans)
        ans.append(root.val)
        self.helper(root.right, ans)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root: return ans
        queue = collections.deque()
        cur = root
        while cur or queue:
            while cur:
                queue.append(cur)
                cur = cur.left
            cur = queue.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
#leetcode submit region end(Prohibit modification and deletion)
