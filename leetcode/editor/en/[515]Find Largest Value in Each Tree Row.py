# You need to find the largest value in each row of a binary tree. 
# 
#  Example: 
#  
# Input: 
# 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# 
# Output: [1, 3, 9]
#  
#  
#  Related Topics Tree Depth-first Search Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root: return ans
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            mx = -float('inf')
            for _ in range(size):
                node = queue.popleft()
                mx = max(mx, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(mx)
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
