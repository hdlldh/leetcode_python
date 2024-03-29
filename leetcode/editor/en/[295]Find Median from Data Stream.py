#Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value. 
#For example,
#
# [2,3,4], the median is 3 
#
# [2,3], the median is (2 + 3) / 2 = 2.5 
#
# Design a data structure that supports the following two operations: 
#
# 
# void addNum(int num) - Add a integer number from the data stream to the data structure. 
# double findMedian() - Return the median of all elements so far. 
# 
#
# 
#
# Example: 
#
# 
#addNum(1)
#addNum(2)
#findMedian() -> 1.5
#addNum(3) 
#findMedian() -> 2
# 
#
# 
#
# Follow up: 
#
# 
# If all integer numbers from the stream are between 0 and 100, how would you optimize it? 
# If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it? 
# 
# Related Topics Heap Design


import heapq
#leetcode submit region begin(Prohibit modification and deletion)
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.maxHeap, -num)
        val = heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, -val)
        if len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0]-self.maxHeap[0])*0.5
        else:
            return -self.maxHeap[0]*1.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
#leetcode submit region end(Prohibit modification and deletion)
