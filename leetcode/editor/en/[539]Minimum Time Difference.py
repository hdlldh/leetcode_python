#Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list. 
#
# Example 1: 
# 
#Input: ["23:59","00:00"]
#Output: 1
# 
# 
#
# Note: 
# 
# The number of time points in the given list is at least 2 and won't exceed 20000. 
# The input time is legal and ranges from 00:00 to 23:59. 
# 
# Related Topics String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints.sort()
        ans = float('inf')
        n = len(timePoints)
        for i in range(1, n):
            gap = self.findGap(timePoints[i-1], timePoints[i])
            ans = min(ans, gap)
        gap = self.findGap(timePoints[0], timePoints[-1])
        ans = min(ans, 24*60-gap)
        return ans


    def findGap(self, x, y):
        h1, m1 = x.split(':')
        h2, m2 = y.split(':')
        return (int(h2)-int(h1))*60+(int(m2)-int(m1))
        
#leetcode submit region end(Prohibit modification and deletion)
