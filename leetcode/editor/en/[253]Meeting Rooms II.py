#Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required. 
#
# Example 1: 
#
# 
#Input: [[0, 30],[5, 10],[15, 20]]
#Output: 2 
#
# Example 2: 
#
# 
#Input: [[7,10],[2,4]]
#Output: 1 
#
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature. 
# Related Topics Heap Greedy Sort


import heapq
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        if n<=1: return n
        intervals.sort(key= lambda x: x[0])
        heap = []
        rooms = 0
        for i in range(n):
            while heap and heap[0][0]<= intervals[i][0]:
                heapq.heappop(heap)
            heapq.heappush(heap,[intervals[i][1], intervals[i][0]])
            rooms = max(rooms, len(heap))
        return rooms
        
#leetcode submit region end(Prohibit modification and deletion)
