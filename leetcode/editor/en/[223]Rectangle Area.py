#Find the total area covered by two rectilinear rectangles in a 2D plane. 
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure. 
#
# 
#
# Example: 
#
# 
#Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
#Output: 45 
#
# Note: 
#
# Assume that the total area is never beyond the maximum possible value of int. 
# Related Topics Math



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        s1 = (C-A) * (D-B)
        s2 = (G-E) * (H-F)
        if min(C, G) > max(A, E) and min(D, H) > max(B, F):
            return s1 + s2 - (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        else:
            return s1 + s2
        
#leetcode submit region end(Prohibit modification and deletion)
