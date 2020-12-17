#Two players play a turn based game on a binary tree. We are given the root of t
#his binary tree, and the number of nodes n in the tree. n is odd, and each node 
#has a distinct value from 1 to n. 
#
# Initially, the first player names a value x with 1 <= x <= n, and the second p
#layer names a value y with 1 <= y <= n and y != x. The first player colors the n
#ode with value x red, and the second player colors the node with value y blue. 
#
# Then, the players take turns starting with the first player. In each turn, tha
#t player chooses a node of their color (red if player 1, blue if player 2) and c
#olors an uncolored neighbor of the chosen node (either the left child, right chi
#ld, or parent of the chosen node.) 
#
# If (and only if) a player cannot choose such a node in this way, they must pas
#s their turn. If both players pass their turn, the game ends, and the winner is 
#the player that colored more nodes. 
#
# You are the second player. If it is possible to choose such a y to ensure you 
#win the game, return true. If it is not possible, return false. 
#
# 
# Example 1: 
#
# 
#Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
#Output: true
#Explanation: The second player can choose the node with value 2.
# 
#
# 
# Constraints: 
#
# 
# root is the root of a binary tree with n nodes and distinct node values from 1
# to n. 
# n is odd. 
# 1 <= x <= n <= 100 
# 
# Related Topics Tree Depth-first Search




#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        red = self.find(root, x)
        left = self.size(red.left)
        right = self.size(red.right)
        parent = n - left - right - 1
        if left > n // 2 or right > n // 2 or parent > n // 2: return True
        return False

    def size(self, root):
        if not root: return 0
        return self.size(root.left) + self.size(root.right) + 1

    def find(self, root, val):
        if not root: return None
        if root.val == val: return root
        left = self.find(root.left, val)
        right = self.find(root.right, val)
        if left is not None: return left
        if right is not None: return right
        return None
        
#leetcode submit region end(Prohibit modification and deletion)
