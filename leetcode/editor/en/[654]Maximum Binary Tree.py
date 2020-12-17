#
#Given an integer array with no duplicates. A maximum tree building on this arra
#y is defined as follow:
# 
# The root is the maximum number in the array. 
# The left subtree is the maximum tree constructed from left part subarray divid
#ed by the maximum number. 
# The right subtree is the maximum tree constructed from right part subarray div
#ided by the maximum number. 
# 
# 
#
# 
#Construct the maximum tree by the given array and output the root node of this 
#tree.
# 
#
# Example 1: 
# 
#Input: [3,2,1,6,0,5]
#Output: return the tree root node representing the following tree:
#
#      6
#    /   \
#   3     5
#    \    / 
#     2  0   
#       \
#        1
# 
# 
#
# Note: 
# 
# The size of the given array will be in the range [1,1000]. 
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
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, l, r):
        if l>r: return None
        mx = -float('inf')
        mk = 0
        for k in range(l, r+1):
            if nums[k]>mx:
                mx = nums[k]
                mk = k
        node = TreeNode(mx)
        node.left = self.helper(nums, l, mk-1)
        node.right = self.helper(nums, mk+1, r)
        return node
        
#leetcode submit region end(Prohibit modification and deletion)
