# Given the root of a binary tree, find the maximum value V for which there exis
# ts different nodes A and B where V = |A.val - B.val| and A is an ancestor of B. 
# 
# 
#  (A node A is an ancestor of B if either: any child of A is equal to B, or any
#  child of A is an ancestor of B.) 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: 
# We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| 
# = 7.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The number of nodes in the tree is between 2 and 5000. 
#  Each node will have value between 0 and 100000. 
#  
#  Related Topics Tree Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        queue = collections.deque()
        queue.append([root, root.val, root.val])
        while queue:
            node, left, right = queue.popleft()
            if node.left:
                val = node.left.val
                ans = max(ans, abs(val-left), abs(val-right))
                queue.append([node.left, min(left, val), max(right, val)])
            if node.right:
                val = node.right.val
                ans = max(ans, abs(val-left), abs(val-right))
                queue.append([node.right, min(left, val), max(right, val)])
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
