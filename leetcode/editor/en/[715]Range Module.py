#A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner. 
#
# addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked. 
#
# queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right)
# is currently being tracked. 
#
# removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right). 
#
# Example 1: 
# 
#addRange(10, 20): null
#removeRange(14, 16): null
#queryRange(10, 14): true (Every number in [10, 14) is being tracked)
#queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
#queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
# 
# 
#
# Note:
# A half open interval [left, right) denotes all real numbers left <= x < right. 
#
# 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange. 
# The total number of calls to addRange in a single test case is at most 1000. 
# The total number of calls to queryRange in a single test case is at most 5000. 
# The total number of calls to removeRange in a single test case is at most 1000. 
# Related Topics Segment Tree Ordered Map


import bisect
#leetcode submit region begin(Prohibit modification and deletion)
class RangeModule(object):

    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        new_ranges = []
        bisect.insort_left(self.ranges, [left, right])
        for i in range(len(self.ranges)):
            if not new_ranges or self.ranges[i][0]>new_ranges[-1][1]:
                new_ranges.append(self.ranges[i])
            else:
                new_ranges[-1][1] = max(new_ranges[-1][1], self.ranges[i][1])
        self.ranges = new_ranges

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        low = 0
        high = len(self.ranges)-1
        while low<=high:
            mid = low + (high-low)//2
            if self.ranges[mid][0] > right: high = mid-1
            elif self.ranges[mid][1] < left: low = mid +1
            else:
                return self.ranges[mid][0]<=left and self.ranges[mid][1]>=right
        return False
        

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        new_ranges = []
        for i in range(len(self.ranges)):
            if self.ranges[i][1]<=left or self.ranges[i][0] >=right:
                new_ranges.append(self.ranges[i])
            else:
                if self.ranges[i][0]< left: new_ranges.append([self.ranges[i][0], left])
                if self.ranges[i][1]> right: new_ranges.append([right, self.ranges[i][1]])
        self.ranges = new_ranges
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
#leetcode submit region end(Prohibit modification and deletion)
