#Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array. 
#
# Note: 
#The array size can be very large. Solution that uses too much extra space will not pass the judge. 
#
# Example: 
#
# 
#int[] nums = new int[] {1,2,3,3,3};
#Solution solution = new Solution(nums);
#
#// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
#solution.pick(3);
#
#// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
#solution.pick(1);
# 
# Related Topics Reservoir Sampling

import random

#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        ans = None
        for i, num in enumerate(self.nums):
            if num == target:
                count +=1
                if count==1:
                    ans = i
                else:
                    p = random.randrange(count)
                    if p==0: ans = i
        return ans


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
#leetcode submit region end(Prohibit modification and deletion)
