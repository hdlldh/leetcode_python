# A boomerang is a set of 3 points that are all distinct and not in a straight l
# ine. 
# 
#  Given a list of three points in the plane, return whether these points are a 
# boomerang. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [[1,1],[2,3],[3,2]]
# Output: true
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [[1,1],[2,2],[3,3]]
# Output: false 
#  
# 
#  
# 
#  Note: 
# 
#  
#  points.length == 3 
#  points[i].length == 2 
#  0 <= points[i][j] <= 100 
#  
# 
#  
#  
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """

        def gcd(a, b):
            if b == 0: return a
            return gcd(b, a % b)

        hashset = set()
        for i in range(3):
            for j in range(i + 1, 3):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if x == 0 and y == 0: return False
                # if y<0:
                #    x = -x
                #    y = -y
                d = gcd(x, y)
                x = x // d
                y = y // d
                hashset.add((x, y))
        return len(hashset) == 3
        
# leetcode submit region end(Prohibit modification and deletion)
