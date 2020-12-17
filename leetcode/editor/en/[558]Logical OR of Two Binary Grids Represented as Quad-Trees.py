# A Binary Matrix is a matrix in which all the elements are either 0 or 1. 
# 
#  Given quadTree1 and quadTree2. quadTree1 represents a n * n binary matrix and
#  quadTree2 represents another n * n binary matrix. 
# 
#  Return a Quad-Tree representing the n * n binary matrix which is the result o
# f logical bitwise OR of the two binary matrixes represented by quadTree1 and qua
# dTree2. 
# 
#  Notice that you can assign the value of a node to True or False when isLeaf i
# s False, and both are accepted in the answer. 
# 
#  A Quad-Tree is a tree data structure in which each internal node has exactly 
# four children. Besides, each node has two attributes: 
# 
#  
#  val: True if the node represents a grid of 1's or False if the node represent
# s a grid of 0's. 
#  isLeaf: True if the node is leaf node on the tree or False if the node has th
# e four children. 
#  
# 
#  
# class Node {
#     public boolean val;
#     public boolean isLeaf;
#     public Node topLeft;
#     public Node topRight;
#     public Node bottomLeft;
#     public Node bottomRight;
# } 
# 
#  We can construct a Quad-Tree from a two-dimensional area using the following 
# steps: 
# 
#  
#  If the current grid has the same value (i.e all 1's or all 0's) set isLeaf Tr
# ue and set val to the value of the grid and set the four children to Null and st
# op. 
#  If the current grid has different values, set isLeaf to False and set val to 
# any value and divide the current grid into four sub-grids as shown in the photo.
#  
#  Recurse for each of the children with the proper sub-grid. 
#  
# 
#  If you want to know more about the Quad-Tree, you can refer to the wiki. 
# 
#  Quad-Tree format: 
# 
#  The input/output represents the serialized format of a Quad-Tree using level 
# order traversal, where null signifies a path terminator where no node exists bel
# ow. 
# 
#  It is very similar to the serialization of the binary tree. The only differen
# ce is that the node is represented as a list [isLeaf, val]. 
# 
#  If the value of isLeaf or val is True we represent it as 1 in the list [isLea
# f, val] and if the value of isLeaf or val is False we represent it as 0. 
# 
#  
#  Example 1: 
#  
#  
# Input: quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]
# , quadTree2 = [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[
# 1,1],[1,1]]
# Output: [[0,0],[1,1],[1,1],[1,1],[1,0]]
# Explanation: quadTree1 and quadTree2 are shown above. You can see the binary m
# atrix which is represented by each Quad-Tree.
# If we apply logical bitwise OR on the two binary matrices we get the binary ma
# trix below which is represented by the result Quad-Tree.
# Notice that the binary matrices shown are only for illustration, you don't hav
# e to construct the binary matrix to get the result tree.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: quadTree1 = [[1,0]]
# , quadTree2 = [[1,0]]
# Output: [[1,0]]
# Explanation: Each tree represents a binary matrix of size 1*1. Each matrix con
# tains only zero.
# The resulting matrix is of size 1*1 with also zero.
#  
# 
#  Example 3: 
# 
#  
# Input: quadTree1 = [[0,0],[1,0],[1,0],[1,1],[1,1]]
# , quadTree2 = [[0,0],[1,1],[1,1],[1,0],[1,1]]
# Output: [[1,1]]
#  
# 
#  Example 4: 
# 
#  
# Input: quadTree1 = [[0,0],[1,1],[1,0],[1,1],[1,1]]
# , quadTree2 = [[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[
# 1,0],[1,1]]
# Output: [[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,0],[
# 1,1]]
#  
# 
#  Example 5: 
# 
#  
# Input: quadTree1 = [[0,1],[1,0],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1
# ,0],[1,1],[1,1]]
# , quadTree2 = [[0,1],[0,1],[1,0],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1]]
# Output: [[0,0],[0,1],[0,1],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1],[1,0],[1,0],[1,
# 1],[1,1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  quadTree1 and quadTree2 are both valid Quad-Trees each representing a n * n g
# rid. 
#  n == 2^x where 0 <= x <= 9. 
#  
# 


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        if tl.val==tr.val==bl.val==br.val and tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf:
            return Node(tl.val, True, None, None, None, None)
        else:
            return Node(False, False, tl, tr, bl, br)
        
# leetcode submit region end(Prohibit modification and deletion)
