#Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. 
#
# Example: 
#
# 
#Input:  [1,2,1,3,2,5]
#Output: [3,5] 
#
# Note: 
#
# 
# The order of the result is not important. So in the above example, [5, 3] is also correct. 
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity? 
# Related Topics Bit Manipulation



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        s = 0
        for num in nums:
            s ^= num

        s &= -s
        a, b = 0, 0
        for num in nums:
            if num & s:
                a ^= num
            else:
                b ^= num
        return [a, b]
#leetcode submit region end(Prohibit modification and deletion)
