#Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window. 
#
# Example: 
#
# 
#MovingAverage m = new MovingAverage(3);
#m.next(1) = 1
#m.next(10) = (1 + 10) / 2
#m.next(3) = (1 + 10 + 3) / 3
#m.next(5) = (10 + 3 + 5) / 3
# 
#
# 
# Related Topics Design Queue


import collections
#leetcode submit region begin(Prohibit modification and deletion)
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque()
        self.size = size
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue)==self.size:
            num = self.queue.popleft()
            self.sum -= num
        self.queue.append(val)
        self.sum += val
        return float(self.sum)/len(self.queue)


        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
#leetcode submit region end(Prohibit modification and deletion)
