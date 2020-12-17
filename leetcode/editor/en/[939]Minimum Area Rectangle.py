# Given a set of points in the xy-plane, determine the minimum area of a rectang
# le formed from these points, with sides parallel to the x and y axes. 
# 
#  If there isn't any rectangle, return 0. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= points.length <= 500 
#  0 <= points[i][0] <= 40000 
#  0 <= points[i][1] <= 40000 
#  All points are distinct. 
#  
#  
#  Related Topics Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        min_area = float('inf')
        point_set = set()
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1==x2 or y1==y2: continue
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    min_area = min(min_area, abs(x1-x2)*abs(y1-y2))
                point_set.add((x1, y1))
                point_set.add((x2, y2))
        return min_area if min_area<float('inf') else 0
        
# leetcode submit region end(Prohibit modification and deletion)
