#There are a number of spherical balloons spread in two-dimensional space. For e
#ach balloon, provided input is the start and end coordinates of the horizontal d
#iameter. Since it's horizontal, y-coordinates don't matter and hence the x-coord
#inates of start and end of the diameter suffice. Start is always smaller than en
#d. There will be at most 104 balloons. 
#
# An arrow can be shot up exactly vertically from different points along the x-a
#xis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤
# xend. There is no limit to the number of arrows that can be shot. An arrow once
# shot keeps travelling up infinitely. The problem is to find the minimum number 
#of arrows that must be shot to burst all balloons. 
#
# Example: 
#
# 
#Input:
#[[10,16], [2,8], [1,6], [7,12]]
#
#Output:
#2
#
#Explanation:
#One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8]
# and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
# 
#
# 
# Related Topics Greedy




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n==0: return 0
        points.sort(key=lambda x: x[1])
        ans = 1
        p = points[0][1]
        for i in range(1, n):
            if points[i][0]> p:
                p = points[i][1]
                ans += 1
        return ans

#leetcode submit region end(Prohibit modification and deletion)
