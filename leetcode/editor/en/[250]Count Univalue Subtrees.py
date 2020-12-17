#Given a binary tree, count the number of uni-value subtrees. 
#
# A Uni-value subtree means all nodes of the subtree have the same value. 
#
# Example : 
#
# 
#Input:  root = [5,1,5,5,5,null,5]
#
#              5
#             / \
#            1   5
#           / \   \
#          5   5   5
#
#Output: 4
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
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root: return [True, None]
        left, leftV = self.helper(root.left)
        right, rightV = self.helper(root.right)
        if left and right and (leftV is None or leftV == root.val) and (rightV is None or rightV == root.val):
            self.ans += 1
            return [True, root.val]
        return [False, root.val]
        
#leetcode submit region end(Prohibit modification and deletion)
