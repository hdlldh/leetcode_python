# Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b]
#  represents the set of real numbers x such that a <= x < b. 
# 
#  We remove the intersections between any interval in intervals and the interva
# l toBeRemoved. 
# 
#  Return a sorted list of intervals after all such removals. 
# 
#  
#  Example 1: 
#  Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
# Output: [[0,1],[6,7]]
#  Example 2: 
#  Input: intervals = [[0,5]], toBeRemoved = [2,3]
# Output: [[0,2],[3,5]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 10^4 
#  -10^9 <= intervals[i][0] < intervals[i][1] <= 10^9 
#  
#  Related Topics Math Line Sweep


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        
# leetcode submit region end(Prohibit modification and deletion)
