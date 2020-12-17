# Given a binary tree where each path going from the root to any leaf form a val
# id sequence, check if a given string is a valid sequence in such binary tree. 
# 
#  We get the given string from the concatenation of an array of integers arr an
# d the concatenation of all values of the nodes along a path results in a sequenc
# e in the given binary tree. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation: 
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
# Other valid sequences are: 
# 0 -> 1 -> 1 -> 0 
# 0 -> 0 -> 0
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
# Output: false 
# Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a s
# equence.
#  
# 
#  Example 3: 
# 
#  
# 
#  
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
# Output: false
# Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequenc
# e.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 5000 
#  0 <= arr[i] <= 9 
#  Each node's value is between [0 - 9]. 
#  
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        
# leetcode submit region end(Prohibit modification and deletion)
