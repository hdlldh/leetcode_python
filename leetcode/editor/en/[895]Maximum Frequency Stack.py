# Implement FreqStack, a class which simulates the operation of a stack-like dat
# a structure. 
# 
#  FreqStack has two functions: 
# 
#  
#  push(int x), which pushes an integer x onto the stack. 
#  pop(), which removes and returns the most frequent element in the stack.
#  
#  If there is a tie for most frequent element, the element closest to the top o
# f the stack is removed and returned. 
#  
#  
#  
# 
#  
# 
#  Example 1: 
# 
#  
# Input: 
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"
# ],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to t
# op.  Then:
# 
# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].
# 
# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the t
# op.
# The stack becomes [5,7,5,4].
# 
# pop() -> returns 5.
# The stack becomes [5,7,4].
# 
# pop() -> returns 4.
# The stack becomes [5,7].
#  
# 
#  
# 
#  Note: 
# 
#  
#  Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9. 
#  It is guaranteed that FreqStack.pop() won't be called if the stack has zero e
# lements. 
#  The total number of FreqStack.push calls will not exceed 10000 in a single te
# st case. 
#  The total number of FreqStack.pop calls will not exceed 10000 in a single tes
# t case. 
#  The total number of FreqStack.push and FreqStack.pop calls will not exceed 15
# 0000 across all test cases. 
#  
# 
#  
#  
#  
#  Related Topics Hash Table Stack


# leetcode submit region begin(Prohibit modification and deletion)
class FreqStack(object):

    def __init__(self):
        self.stack = []
        self.count = {}
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x not in self.count: self.count[x] = 0
        else: self.count[x] += 1
        if len(self.stack) == self.count[x]: self.stack.append([])
        self.stack[self.count[x]].append(x)

    def pop(self):
        """
        :rtype: int
        """
        val = self.stack[-1].pop()
        if not self.stack[-1]: self.stack.pop()
        self.count[val] -= 1
        if self.count[val] < 0: self.count.pop(val)
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
# leetcode submit region end(Prohibit modification and deletion)
