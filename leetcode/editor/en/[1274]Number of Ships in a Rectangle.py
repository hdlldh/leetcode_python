# (This problem is an interactive problem.) 
# 
#  On the sea represented by a cartesian plane, each ship is located at an integ
# er point, and each integer point may contain at most 1 ship. 
# 
#  You have a function Sea.hasShips(topRight, bottomLeft) which takes two points
#  as arguments and returns true if and only if there is at least one ship in the 
# rectangle represented by the two points, including on the boundary. 
# 
#  Given two points, which are the top right and bottom left corners of a rectan
# gle, return the number of ships present in that rectangle. It is guaranteed that
#  there are at most 10 ships in that rectangle. 
# 
#  Submissions making more than 400 calls to hasShips will be judged Wrong Answe
# r. Also, any solutions that attempt to circumvent the judge will result in disqu
# alification. 
# 
#  
#  Example : 
# 
#  
# 
#  
# Input: 
# ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
# Output: 3
# Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
#  
# 
#  
#  Constraints: 
# 
#  
#  On the input ships is only given to initialize the map internally. You must s
# olve this problem "blindfolded". In other words, you must find the answer using 
# the given hasShips API, without knowing the ships position. 
#  0 <= bottomLeft[0] <= topRight[0] <= 1000 
#  0 <= bottomLeft[1] <= topRight[1] <= 1000 
#  
#  Related Topics Divide and Conquer


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        
# leetcode submit region end(Prohibit modification and deletion)
