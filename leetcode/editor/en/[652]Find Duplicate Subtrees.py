#Given a binary tree, return all duplicate subtrees. For each kind of duplicate 
#subtrees, you only need to return the root node of any one of them. 
#
# Two trees are duplicate if they have the same structure with same node values.
# 
#
# Example 1: 
#
# 
#        1
#       / \
#      2   3
#     /   / \
#    4   2   4
#       /
#      4
# 
#
# The following are two duplicate subtrees: 
#
# 
#      2
#     /
#    4
# 
#
# and 
#
# 
#    4
# 
#Therefore, you need to return above trees' root in the form of a list. Related 
#Topics Tree




#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        ans = []
        mem = {}
        self.serialize(root, mem, ans)
        return ans

    def serialize(self, root, mem, ans):
        if not root: return "#"
        key = str(root.val)+","+self.serialize(root.left, mem, ans) +"," + self.serialize(root.right, mem, ans)
        if key not in mem: mem[key] =1
        else: mem[key]+=1
        if mem[key] ==2: ans.append(root)
        return key

#leetcode submit region end(Prohibit modification and deletion)
