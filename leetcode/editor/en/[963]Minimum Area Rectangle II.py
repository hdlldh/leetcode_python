# Given a set of points in the xy-plane, determine the minimum area of any recta
# ngle formed from these points, with sides not necessarily parallel to the x and 
# y axes. 
# 
#  If there isn't any rectangle, return 0. 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: [[1,2],[2,1],[1,0],[0,1]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], wit
# h an area of 2.
#  
# 
#  
#  Example 2: 
# 
#  
# 
#  
# Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
# Output: 1.00000
# Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], wit
# h an area of 1.
#  
# 
#  
#  Example 3: 
# 
#  
# 
#  
# Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
# Output: 0
# Explanation: There is no possible rectangle to form from these points.
#  
# 
#  
#  Example 4: 
# 
#  
# 
#  
# Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], wit
# h an area of 2.
#  
#  
# 
#  
#  
#  
# 
#  Note: 
# 
#  
#  1 <= points.length <= 50 
#  0 <= points[i][0] <= 40000 
#  0 <= points[i][1] <= 40000 
#  All points are distinct. 
#  Answers within 10^-5 of the actual value will be accepted as correct. 
#  
#  Related Topics Math Geometry


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(points)
        mem = set()
        ans = float('inf')
        for i in range(n): mem.add((points[i][0],points[i][1]))
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1,n):
                x2, y2 = points[j][0], points[j][1]
                for k in range(j+1, n):
                    x3, y3 = points[k][0], points[k][1]
                    x4 = x1 + x2 - x3
                    y4 = y1 + y2 - y3
                    v12 = (x1-x2)**2+(y1-y2)**2
                    v34 = (x3-x4)**2+(y3-y4)**2
                    if  (x4, y4) in mem and v12 == v34:
                        v13 = (x1-x3)**2+(y1-y3)**2
                        v14 = (x1-x4)**2+(y1-y4)**2
                        ans = min(ans, (v13*v14)**0.5)
        if ans < float('inf'): return ans
        return 0
        
# leetcode submit region end(Prohibit modification and deletion)
