#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. 
#
# 
# push(x) -- Push element x onto stack. 
# pop() -- Removes the element on top of the stack. 
# top() -- Get the top element. 
# getMin() -- Retrieve the minimum element in the stack. 
# 
#
# 
#
# Example: 
#
# 
#MinStack minStack = new MinStack();
#minStack.push(-2);
#minStack.push(0);
#minStack.push(-3);
#minStack.getMin();   --> Returns -3.
#minStack.pop();
#minStack.top();      --> Returns 0.
#minStack.getMin();   --> Returns -2.
# 
#
# 
# Related Topics Stack Design



#leetcode submit region begin(Prohibit modification and deletion)
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack =[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack: self.stack.append((x,x))
        else:
            if x < self.stack[-1][1]: self.stack.append((x,x))
            else: self.stack.append((x, self.stack[-1][1]))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
#leetcode submit region end(Prohibit modification and deletion)
