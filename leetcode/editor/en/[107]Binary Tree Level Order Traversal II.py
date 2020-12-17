#Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root). 
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
#return its bottom-up level order traversal as: 
# 
#[
#  [15,7],
#  [9,20],
#  [3]
#]
# 
# Related Topics Tree Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root: return ans
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.insert(0,level[:])
        return ans
#leetcode submit region end(Prohibit modification and deletion)
