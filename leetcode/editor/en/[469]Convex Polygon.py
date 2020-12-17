# Given a list of points that form a polygon when joined sequentially, find if t
# his polygon is convex (Convex polygon definition). 
# 
#  
# 
#  Note: 
# 
#  
#  There are at least 3 and at most 10,000 points. 
#  Coordinates are in the range -10,000 to 10,000. 
#  You may assume the polygon formed by given points is always a simple polygon 
# (Simple polygon definition). In other words, we ensure that exactly two edges in
# tersect at each vertex, and that edges otherwise don't intersect each other. 
#  
# 
#  
# 
#  Example 1: 
# 
#  
# [[0,0],[0,1],[1,1],[1,0]]
# 
# Answer: True
# 
# Explanation:
#  
# 
#  Example 2: 
# 
#  
# [[0,0],[0,10],[10,10],[10,0],[5,5]]
# 
# Answer: False
# 
# Explanation:
#  
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        n = len(points)
        pre = 0
        for i in range(n):
            x0, y0 = points[i]
            x1, y1 = points[(i+1)%n]
            x2, y2 = points[(i+2)%n]
            dx1, dy1 = x1 - x0, y1 - y0
            dx2, dy2 = x2 - x1, y2 - y1
            cur = dx1 * dy2 - dx2 * dy1
            if cur != 0:
                if cur * pre <0:return False
                else: pre = cur
        return True
        
# leetcode submit region end(Prohibit modification and deletion)
