#Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive. 
#
# Example: 
# 
#Given nums = [-2, 0, 3, -5, 2, -1]
#
#sumRange(0, 2) -> 1
#sumRange(2, 5) -> -1
#sumRange(0, 5) -> -3
# 
# 
#
# Note: 
# 
# You may assume that the array does not change. 
# There are many calls to sumRange function. 
# 
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data= [0]
        for num in nums:
            self.data.append(self.data[-1]+num)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.data[j+1]-self.data[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
#leetcode submit region end(Prohibit modification and deletion)
