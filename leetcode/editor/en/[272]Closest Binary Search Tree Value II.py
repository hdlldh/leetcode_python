#Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target. 
#
# Note: 
#
# 
# Given target value is a floating point. 
# You may assume k is always valid, that is: k ≤ total nodes. 
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target. 
# 
#
# Example: 
#
# 
#Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
#
#    4
#   / \
#  2   5
# / \
#1   3
#
#Output: [4,3] 
#
# Follow up: 
#Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)? 
# Related Topics Stack Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        maxQueue = []

        def preorder(root, maxQueue):
            if root is None: return
            heapq.heappush(maxQueue, (-abs(root.val - target), root.val))
            if len(maxQueue) > k:
                heapq.heappop(maxQueue)
            preorder(root.left, maxQueue)
            preorder(root.right, maxQueue)

        preorder(root, maxQueue)
        ans = [x[1] for x in maxQueue]
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
