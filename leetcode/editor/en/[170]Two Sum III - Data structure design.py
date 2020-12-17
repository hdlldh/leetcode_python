#Design and implement a TwoSum class. It should support the following operations: add and find. 
#
# add - Add the number to an internal data structure. 
#find - Find if there exists any pair of numbers which sum is equal to the value. 
#
# Example 1: 
#
# 
#add(1); add(3); add(5);
#find(4) -> true
#find(7) -> false
# 
#
# Example 2: 
#
# 
#add(3); add(1); add(2);
#find(3) -> true
#find(6) -> false 
# Related Topics Hash Table Design



#leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(int)
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.data[number] += 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num1 in self.data:
            num2 = value - num1
            if num1==num2:
                if self.data[num1]>=2: return True
            else:
                if num2 in self.data: return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
#leetcode submit region end(Prohibit modification and deletion)
