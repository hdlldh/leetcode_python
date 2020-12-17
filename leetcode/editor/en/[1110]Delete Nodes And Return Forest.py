# Given the root of a binary tree, each node in the tree has a distinct value. 
# 
#  After deleting all nodes with a value in to_delete, we are left with a forest
#  (a disjoint union of trees). 
# 
#  Return the roots of the trees in the remaining forest. You may return the res
# ult in any order. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the given tree is at most 1000. 
#  Each node has a distinct value between 1 and 1000. 
#  to_delete.length <= 1000 
#  to_delete contains distinct values between 1 and 1000. 
#  Related Topics Tree Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """

        ans = []
        to_del = set(to_delete)
        def dfs(root, to_del, ans):
            if not root: return None
            root.left = dfs(root.left, to_del, ans)
            root.right = dfs(root.right, to_del, ans)
            if root.val not in to_del: return root
            if root.left: ans.append(root.left)
            if root.right: ans.append(root.right)
            return None
        root = dfs(root, to_del, ans)
        if root: ans.append(root)
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
