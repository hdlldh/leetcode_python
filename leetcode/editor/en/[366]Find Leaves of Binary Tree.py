#Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty. 
#
# 
#
# Example: 
#
# 
#Input: [1,2,3,4,5]
#  
#          1
#         / \
#        2   3
#       / \     
#      4   5    
#
#Output: [[4,5,3],[2],[1]]
# 
#
# 
#
# Explanation: 
#
# 1. Removing the leaves [4,5,3] would result in this tree: 
#
# 
#          1
#         / 
#        2          
# 
#
# 
#
# 2. Now removing the leaf [2] would result in this tree: 
#
# 
#          1          
# 
#
# 
#
# 3. Now removing the leaf [1] would result in the empty tree: 
#
# 
#          []         
# Related Topics Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        hmap = collections.defaultdict(list)
        maxLevel = self.helper(root, hmap)
        ans = []
        for level in range(maxLevel, 0, -1):
            ans.append(hmap[level])
        return ans

    def helper(self, root, hmap):
        if not root: return 0
        if not root.left and not root.right:
            hmap[1].append(root.val)
            return 1
        left = self.helper(root.left, hmap)
        right = self.helper(root.right, hmap)
        level = max(left, right) + 1
        hmap[level].append(root.val)
        return level
        
#leetcode submit region end(Prohibit modification and deletion)
