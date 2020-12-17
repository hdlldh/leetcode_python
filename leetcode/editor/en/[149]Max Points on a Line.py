#Given n points on a 2D plane, find the maximum number of points that lie on the same straight line. 
#
# Example 1: 
#
# 
#Input: [[1,1],[2,2],[3,3]]
#Output: 3
#Explanation:
#^
#|
#|        o
#|     o
#|  o  
#+------------->
#0  1  2  3  4
# 
#
# Example 2: 
#
# 
#Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
#Output: 4
#Explanation:
#^
#|
#|  o
#|     o        o
#|        o
#|  o        o
#+------------------->
#0  1  2  3  4  5  6
# 
#
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature. 
# Related Topics Hash Table Math



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n == 0: return 0

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        res = 0
        for i in range(n):
            duplicates = 1
            hashmap = collections.defaultdict(int)
            for j in range(n):
                if i == j: continue
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    duplicates += 1
                    continue
                else:
                    dx = points[j][0] - points[i][0]
                    dy = points[j][1] - points[i][1]
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    d = gcd(dx, dy)
                    dx = dx // d
                    dy = dy // d
                    hashmap[(dx, dy)] += 1

            res = max(res, duplicates)
            for v in hashmap.values():
                res = max(res, duplicates + v)

        return res
#leetcode submit region end(Prohibit modification and deletion)
