#Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. 
#
# Note: The algorithm should run in linear time and in O(1) space. 
#
# Example 1: 
#
# 
#Input: [3,2,3]
#Output: [3] 
#
# Example 2: 
#
# 
#Input: [1,1,1,3,3,2,2,2]
#Output: [1,2] 
# Related Topics Array



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        n1 = None
        n2 = None
        c1 = 0
        c2 = 0
        ans = []

        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1 = num
                c1 = 1
            elif c2 == 0:
                n2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        c1 = c2 = c3 = 0
        for num in nums:
            if num == n1: c1+=1
            elif num == n2: c2+=1

        if c1*3 > n: ans.append(n1)
        if c2*3 > n: ans.append(n2)
        return ans



        
#leetcode submit region end(Prohibit modification and deletion)
