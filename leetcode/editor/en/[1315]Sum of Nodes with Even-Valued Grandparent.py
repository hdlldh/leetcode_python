# Given a binary tree, return the sum of values of nodes with even-valued grandp
# arent. (A grandparent of a node is the parent of its parent, if it exists.) 
# 
#  If there are no nodes with an even-valued grandparent, return 0. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the
#  blue nodes are the even-value grandparents.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is between 1 and 10^4. 
#  The value of nodes is between 1 and 100. 
#  Related Topics Tree Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if not root: return ans
        queue = collections.deque()
        queue.append([root, None])
        while queue:
            node, par = queue.popleft()
            if node.left:
                if par and par.val %2 == 0:
                    ans += node.left.val
                queue.append([node.left, node])
            if node.right:
                if par and par.val %2 == 0:
                    ans += node.right.val
                queue.append([node.right, node])
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
