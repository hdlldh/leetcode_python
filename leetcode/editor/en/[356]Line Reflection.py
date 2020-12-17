#Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points. 
#
# Example 1: 
#
# 
#Input: [[1,1],[-1,1]]
#Output: true
# 
#
# 
# Example 2: 
#
# 
#Input: [[1,1],[-1,-1]]
#Output: false 
# 
#
# Follow up: 
#Could you do better than O(n2) ? Related Topics Hash Table Math



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        n = len(points)
        if n<=1: return True
        xmin = float('inf')
        xmax = -float('inf')
        hset = set()
        for p in points:
            x, y = p
            xmin = min(xmin, x)
            xmax = max(xmax, x)
            hset.add((x,y))

        for p in points:
            x, y = p
            xr = xmin+xmax-x
            if (xr, y) not in hset: return False

        return True
        
#leetcode submit region end(Prohibit modification and deletion)
