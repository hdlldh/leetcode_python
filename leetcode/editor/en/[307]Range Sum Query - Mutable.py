#Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive. 
#
# The update(i, val) function modifies nums by updating the element at index i to val. 
#
# Example: 
#
# 
#Given nums = [1, 3, 5]
#
#sumRange(0, 2) -> 9
#update(1, 2)
#sumRange(0, 2) -> 8
# 
#
# Note: 
#
# 
# The array is only modifiable by the update function. 
# You may assume the number of calls to update and sumRange function is distributed evenly. 
# 
# Related Topics Binary Indexed Tree Segment Tree



#leetcode submit region begin(Prohibit modification and deletion)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.data = [0]*(2*n)
        self.size = n
        for i in range(n):
            self.data[i+n] = nums[i]
        for i in range(n-1, 0, -1):
            self.data[i] = self.data[2*i] + self.data[2*i+1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        i += self.size
        self.data[i] = val
        while i//2:
            if i%2==0: j = i+1
            else: j = i-1
            self.data[i//2] = self.data[i] + self.data[j]
            i = i//2

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        ans = 0
        i += self.size
        j += self.size
        while i<=j:
            if i%2!=0:
                ans += self.data[i]
                i += 1
            i = i//2
            if j%2==0:
                ans += self.data[j]
                j -= 1
            j = j//2
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
#leetcode submit region end(Prohibit modification and deletion)
