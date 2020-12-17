#Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n. 
#
# Example: 
#
# 
#Input: 3
#Output:
#[
#  [1,null,3,2],
#  [3,2,null,1],
#  [3,1,null,null,2],
#  [2,1,3],
#  [1,null,2,null,3]
#]
#Explanation:
#The above output corresponds to the 5 unique BST's shown below:
#
#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3
# 
# Related Topics Dynamic Programming Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        return self.dfs(1, n)

    def dfs(self, start, end):
        if end < start: return [None]
        ans = []
        for i in range(start, end + 1):
            left = self.dfs(start, i - 1)
            right = self.dfs(i + 1, end)
            for l in left:
                for r in right:
                    node = TreeNode(i, l, r)
                    ans.append(node)
        return ans

#leetcode submit region end(Prohibit modification and deletion)
