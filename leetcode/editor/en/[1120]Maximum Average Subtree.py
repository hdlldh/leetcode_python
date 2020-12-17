# Given the root of a binary tree, find the maximum average value of any subtree
#  of that tree. 
# 
#  (A subtree of a tree is any node of that tree plus all its descendants. The a
# verage value of a tree is the sum of its values, divided by the number of nodes.
# ) 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: [5,6,1]
# Output: 6.00000
# Explanation: 
# For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
# For the node with value = 6 we have an average of 6 / 1 = 6.
# For the node with value = 1 we have an average of 1 / 1 = 1.
# So the answer is 6 which is the maximum.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The number of nodes in the tree is between 1 and 5000. 
#  Each node will have a value between 0 and 100000. 
#  Answers will be accepted as correct if they are within 10^-5 of the correct a
# nswer. 
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
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.ans = -float('inf')
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root: return [0, 0]
        leftSum, leftCnt = self.helper(root.left)
        rightSum, rightCnt = self.helper(root.right)
        curSum = leftSum + rightSum + root.val
        curCnt = leftCnt + rightCnt + 1
        self.ans = max(self.ans, curSum / float(curCnt))
        return [curSum, curCnt]
        
# leetcode submit region end(Prohibit modification and deletion)
