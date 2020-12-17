#Print a binary tree in an m*n 2D string array following these rules: 
#
# 
# The row number m should be equal to the height of the given binary tree. 
# The column number n should always be an odd number. 
# The root node's value (in string format) should be put in the exactly middle o
#f the first row it can be put. The column and the row where the root node belong
#s will separate the rest space into two parts (left-bottom part and right-bottom
# part). You should print the left subtree in the left-bottom part and print the 
#right subtree in the right-bottom part. The left-bottom part and the right-botto
#m part should have the same size. Even if one subtree is none while the other is
# not, you don't need to print anything for the none subtree but still need to le
#ave the space as large as that for the other subtree. However, if two subtrees a
#re none, then you don't need to leave space for both of them. 
# Each unused space should contain an empty string "". 
# Print the subtrees following the same rules. 
# 
#
# Example 1: 
# 
#Input:
#     1
#    /
#   2
#Output:
#[["", "1", ""],
# ["2", "", ""]]
# 
# 
#
#
# Example 2: 
# 
#Input:
#     1
#    / \
#   2   3
#    \
#     4
#Output:
#[["", "", "", "1", "", "", ""],
# ["", "2", "", "", "", "3", ""],
# ["", "", "4", "", "", "", ""]]
# 
# 
#
# Example 3: 
# 
#Input:
#      1
#     / \
#    2   5
#   / 
#  3 
# / 
#4 
#Output:
#
#[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
# ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
# ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
# ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# 
# 
#
# Note:
#The height of binary tree is in the range of [1, 10].
# Related Topics Tree




#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height = self.getHeight(root)
        width = (1<<height) -1
        ans = [[""]*width for _ in range(height)]
        self.fill(root, ans, 0, 0, width-1)
        return ans

    def getHeight(self, root):
        if not root: return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) +1

    def fill(self, root, ans, h, l, r):
        if not root: return
        mid = (l+r)//2
        ans[h][mid] = str(root.val)
        self.fill(root.left, ans, h+1, l, mid-1)
        self.fill(root.right, ans, h+1, mid+1, r)
        
#leetcode submit region end(Prohibit modification and deletion)
