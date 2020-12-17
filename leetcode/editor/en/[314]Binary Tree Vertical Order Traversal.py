#Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column). 
#
# If two nodes are in the same row and column, the order should be from left to right. 
#
# Examples 1: 
#
# 
#Input: [3,9,20,null,null,15,7]
#
#   3
#  /\
# /  \
# 9  20
#    /\
#   /  \
#  15   7 
#
#Output:
#
#[
#  [9],
#  [3,15],
#  [20],
#  [7]
#]
# 
#
# Examples 2: 
#
# 
#Input: [3,9,8,4,0,1,7]
#
#     3
#    /\
#   /  \
#   9   8
#  /\  /\
# /  \/  \
# 4  01   7 
#
#Output:
#
#[
#  [4],
#  [9],
#  [3,0,1],
#  [8],
#  [7]
#]
# 
#
# Examples 3: 
#
# 
#Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
#
#     3
#    /\
#   /  \
#   9   8
#  /\  /\
# /  \/  \
# 4  01   7
#    /\
#   /  \
#   5   2
#
#Output:
#
#[
#  [4],
#  [9,5],
#  [3,0,1],
#  [8,2],
#  [7]
#]
# 
# Related Topics Hash Table



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root: return ans
        queue = collections.deque()
        hmap = collections.defaultdict(list)
        minLevel = 0
        maxLevel = 0
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            minLevel = min(minLevel, level)
            maxLevel = max(maxLevel, level)
            hmap[level].append(node.val)
            if node.left: queue.append((node.left, level-1))
            if node.right: queue.append((node.right, level+1))
        for level in range(minLevel, maxLevel+1):
            ans.append(hmap[level])
        return ans

#leetcode submit region end(Prohibit modification and deletion)
