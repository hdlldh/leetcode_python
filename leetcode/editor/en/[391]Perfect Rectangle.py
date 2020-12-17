#Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region. 
#
# Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)). 
#
# 
#
# Example 1: 
#
# 
#rectangles = [
#  [1,1,3,3],
#  [3,1,4,2],
#  [3,2,4,4],
#  [1,3,2,4],
#  [2,3,3,4]
#]
#
#Return true. All 5 rectangles together form an exact cover of a rectangular region.
# 
#
# 
#
# 
#
# 
#
# Example 2: 
#
# 
#rectangles = [
#  [1,1,2,3],
#  [1,3,2,4],
#  [3,1,4,2],
#  [3,2,4,4]
#]
#
#Return false. Because there is a gap between the two rectangular regions.
# 
#
# 
#
# 
#
# 
#
# Example 3: 
#
# 
#rectangles = [
#  [1,1,3,3],
#  [3,1,4,2],
#  [1,3,2,4],
#  [3,2,4,4]
#]
#
#Return false. Because there is a gap in the top center.
# 
#
# 
#
# 
#
# 
#
# Example 4: 
#
# 
#rectangles = [
#  [1,1,3,3],
#  [3,1,4,2],
#  [1,3,2,4],
#  [2,2,4,4]
#]
#
#Return false. Because two of the rectangles overlap with each other.
# 
#
# Related Topics Line Sweep



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        hmap = collections.defaultdict(int)
        area = 0
        min_x = float('inf')
        min_y = float('inf')
        max_x = -float('inf')
        max_y = -float('inf')
        for bx, by, tx, ty in rectangles:
            hmap[(bx, by)] += 1
            hmap[(tx, ty)] += 1
            hmap[(bx, ty)] += 1
            hmap[(tx, by)] += 1
            area += (tx - bx) * (ty - by)

        count = 0
        for k, v in hmap.items():
            if v == 1:
                count += 1
                min_x = min(min_x, k[0])
                max_x = max(max_x, k[0])
                min_y = min(min_y, k[1])
                max_y = max(max_y, k[1])
            elif v % 2 == 1:
                return False
        return count == 4 and area == (max_x - min_x) * (max_y - min_y)
#leetcode submit region end(Prohibit modification and deletion)
