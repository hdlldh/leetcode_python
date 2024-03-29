# There's a tree, a squirrel, and several nuts. Positions are represented by the
#  cells in a 2D grid. Your goal is to find the minimal distance for the squirrel 
# to collect all the nuts and put them under the tree one by one. The squirrel can
#  only take at most one nut at one time and can move in four directions - up, dow
# n, left and right, to the adjacent cell. The distance is represented by the numb
# er of moves.
#  Example 1: 
# 
#  
# Input: 
# Height : 5
# Width : 7
# Tree position : [2,2]
# Squirrel : [4,4]
# Nuts : [[3,0], [2,5]]
# Output: 12
# Explanation:
# ​​​​​
#  
# 
#  Note: 
# 
#  
#  All given positions won't overlap. 
#  The squirrel can take at most one nut at one time. 
#  The given positions of nuts have no order. 
#  Height and width are positive integers. 3 <= height * width <= 10,000. 
#  The given positions contain at least one nut, only one tree and one squirrel.
#  
#  
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        tree_cnt = {}
        squirrel_cnt = {}
        for x, y in nuts:
            tree_cnt[(x, y)] = abs(tree[0]-x) + abs(tree[1]-y)
            squirrel_cnt[(x, y)] = abs(squirrel[0] -x) + abs(squirrel[1]-y)
        t = sum(tree_cnt.values())*2
        ans = float('inf')
        for x, y in nuts:
            ans = min(ans, t+squirrel_cnt[(x, y)]-tree_cnt[(x, y)])
        return ans


# leetcode submit region end(Prohibit modification and deletion)
