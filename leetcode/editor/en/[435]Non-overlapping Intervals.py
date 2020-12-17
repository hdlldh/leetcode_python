#Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping. 
#
# 
# 
#
# 
#
# Example 1: 
#
# 
#Input: [[1,2],[2,3],[3,4],[1,3]]
#Output: 1
#Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# 
#
# Example 2: 
#
# 
#Input: [[1,2],[1,2],[1,2]]
#Output: 2
#Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# 
#
# Example 3: 
#
# 
#Input: [[1,2],[2,3]]
#Output: 0
#Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
# 
#
# 
#
# Note: 
#
# 
# You may assume the interval's end point is always bigger than its start point. 
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other. 
# 
# Related Topics Greedy



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        n = len(intervals)
        ans = 0
        left = 0
        for i in range(n):
            if intervals[i][0] < intervals[left][1]:
                ans += 1
                if intervals[i][1] < intervals[left][0]:
                    left = i
            else:
                left = i
        return ans

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[1],-x[0]))
        n = len(intervals)
        if n == 0: return 0
        dp = [1] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = dp[i - 1]
            low = 0
            high = i - 1
            while low <= high:
                mid = low + (high - low) // 2
                if intervals[mid][1] > intervals[i][0]:
                    high = mid - 1
                else:
                    low = mid + 1

            if high>=0:
                dp[i] = max(dp[i], dp[high] + 1)
        #print(dp)
        return n - dp[-1]
#leetcode submit region end(Prohibit modification and deletion)
