# Given the coordinates of four points in 2D space, return whether the four poin
# ts could construct a square. 
# 
#  The coordinate (x,y) of a point is represented by an integer array with two i
# ntegers. 
# 
#  Example: 
# 
#  
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
#  
# 
#  
# 
#  Note: 
# 
#  
#  All the input integers are in the range [-10000, 10000]. 
#  A valid square has four equal sides with positive length and four equal angle
# s (90-degree angles). 
#  Input points have no order. 
#  
# 
#  
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        d = []
        points = [p1,p2,p3,p4]
        for i in range(4):
            for j in range(i+1,4):
                d.append(self.distance(points[i],points[j]))
        d.sort()
        if d[0]!=0 and d[0]==d[1]==d[2]==d[3] and d[4]==d[5]:return True
        return False

    def distance(self, p1, p2):
        return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        
# leetcode submit region end(Prohibit modification and deletion)
