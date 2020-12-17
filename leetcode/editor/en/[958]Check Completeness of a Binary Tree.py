# Given a binary tree, determine if it is a complete binary tree. 
# 
#  Definition of a complete binary tree from Wikipedia: 
# In a complete binary tree every level, except possibly the last, is completely
#  filled, and all nodes in the last level are as far left as possible. It can hav
# e between 1 and 2h nodes inclusive at the last level h. 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values 
# {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as 
# possible.
#  
# 
#  
#  Example 2: 
# 
#  
# 
#  
# Input: [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
#  
# 
#  
#  
# 
#  Note: 
# 
#  
#  The tree will have between 1 and 100 nodes. 
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
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        queue = collections.deque()
        queue.append([root, 1])
        count = 0
        last = 0
        while queue:
            node, v = queue.popleft()
            last = v
            count += 1
            if node.left: queue.append([node.left, 2 * v])
            if node.right: queue.append([node.right, 2 * v + 1])

        return count == last
        
# leetcode submit region end(Prohibit modification and deletion)
