#
#Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.
# 
#
# Examples 1 
#Input:
# 
#  5
# /  \
#2   -3
# 
#return [2, -3, 4], since all the values happen only once, return all of them in any order.
# 
#
# Examples 2 
#Input:
# 
#  5
# /  \
#2   -5
# 
#return [2], since 2 happens twice, however -5 only occur once.
# 
#
# Note:
#You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
# Related Topics Hash Table Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        hmap = collections.defaultdict(int)
        self.maxFreq = 0
        self.helper(root, hmap)
        ans = []
        for val in hmap:
            if hmap[val]==self.maxFreq:
                ans.append(val)
        return ans

    def helper(self, root, hmap):
        if not root: return 0
        left = self.helper(root.left, hmap)
        right = self.helper(root.right, hmap)
        val = left+right+root.val
        hmap[val]+=1
        self.maxFreq = max(self.maxFreq, hmap[val])
        return val
#leetcode submit region end(Prohibit modification and deletion)
