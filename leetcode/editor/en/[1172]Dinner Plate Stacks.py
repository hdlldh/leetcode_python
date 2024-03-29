# You have an infinite number of stacks arranged in a row and numbered (left to 
# right) from 0, each of the stacks has the same maximum capacity. 
# 
#  Implement the DinnerPlates class: 
# 
#  
#  DinnerPlates(int capacity) Initializes the object with the maximum capacity o
# f the stacks. 
#  void push(int val) pushes the given positive integer val into the leftmost st
# ack with size less than capacity. 
#  int pop() returns the value at the top of the rightmost non-empty stack and r
# emoves it from that stack, and returns -1 if all stacks are empty. 
#  int popAtStack(int index) returns the value at the top of the stack with the 
# given index and removes it from that stack, and returns -1 if the stack with tha
# t given index is empty. 
#  
# 
#  Example: 
# 
#  
# Input: 
# ["DinnerPlates","push","push","push","push","push","popAtStack","push","push",
# "popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# Output: 
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]
# 
# Explanation: 
# DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // The stacks are now:  2  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 2.  The stacks are now:     4
#                                                        1  3  5
#                                                        ﹈ ﹈ ﹈
# D.push(20);        // The stacks are now: 20  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.push(21);        // The stacks are now: 20  4 21
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.popAtStack(2);   // Returns 21.  The stacks are now:     4
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈ 
# D.pop()            // Returns 5.  The stacks are now:      4
#                                                         1  3 
#                                                         ﹈ ﹈  
# D.pop()            // Returns 4.  The stacks are now:   1  3 
#                                                         ﹈ ﹈   
# D.pop()            // Returns 3.  The stacks are now:   1 
#                                                         ﹈   
# D.pop()            // Returns 1.  There are no stacks.
# D.pop()            // Returns -1.  There are still no stacks.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= capacity <= 20000 
#  1 <= val <= 20000 
#  0 <= index <= 100000 
#  At most 200000 calls will be made to push, pop, and popAtStack. 
#  
#  Related Topics Design


# leetcode submit region begin(Prohibit modification and deletion)
class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.s = []
        self.q = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.q:
            index = heapq.heappop(self.q)
            self.s[index].append(val)
            if len(self.s[index]) < self.capacity:
                heapq.heappush(self.q, index)
        else:
            index = len(self.s)
            self.s.append([val])
            if len(self.s[index]) < self.capacity:
                heapq.heappush(self.q, index)

    def pop(self):
        """
        :rtype: int
        """
        if not self.s: return -1
        index = len(self.s) - 1
        val = self.s[index].pop()
        if self.s[index]:
            heapq.heappush(self.q, index)
        else:
            while index >= 0 and not self.s[index]:
                self.s.pop()
                if index in self.q: self.q.remove(index)
                index -= 1
        return val

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= len(self.s): return -1
        if not self.s[index]: return -1
        if index == len(self.s) - 1: return self.pop()
        val = self.s[index].pop()
        if index not in self.q: heapq.heappush(self.q, index)
        return val

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
# leetcode submit region end(Prohibit modification and deletion)
