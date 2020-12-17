#A full binary tree is a binary tree where each node has exactly 0 or 2 children
#. 
#
# Return a list of all possible full binary trees with N nodes. Each element of 
#the answer is the root node of one possible tree. 
#
# Each node of each tree in the answer must have node.val = 0. 
#
# You may return the final list of trees in any order. 
#
# 
#
# Example 1: 
#
# 
#Input: 7
#Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0
#,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
#Explanation:
#
# 
#
# 
#
# Note: 
#
# 
# 1 <= N <= 20 
# 
# Related Topics Tree Recursion




#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N%2==0: return []
        if N==1: return [TreeNode(0)]
        ans = []
        for i in range(1, N):
            for l in self.allPossibleFBT(i):
                for r in self.allPossibleFBT(N-i-1):
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
