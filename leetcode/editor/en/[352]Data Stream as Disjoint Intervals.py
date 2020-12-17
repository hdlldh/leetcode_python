#Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals. 
#
# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be: 
#
# 
#[1, 1]
#[1, 1], [3, 3]
#[1, 1], [3, 3], [7, 7]
#[1, 3], [7, 7]
#[1, 3], [6, 7]
# 
#
# 
#
# Follow up: 
#
# What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size? 
# Related Topics Binary Search Ordered Map



#leetcode submit region begin(Prohibit modification and deletion)
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.data:
            low = 0
            high = len(self.data)-1
            while low<=high:
                mid = low + (high-low)//2
                if self.data[mid]>=[val, val]: high = mid-1
                else: low = mid + 1
            left = self.data[:low]
            right = self.data[low:]
            t = [val, val]
            if left and left[-1][1]>=val: return
            if right and right[0][0]<=val: return
            if left and left[-1][1]+1 == val:
                t[0] = left[-1][0]
                left.pop()
            if right and right[0][0] == val+1:
                t[1]= right[0][1]
                right.pop(0)
            self.data = left + [t] + right
        else:
            self.data.append([val, val])


    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.data


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
#leetcode submit region end(Prohibit modification and deletion)
